#!/usr/bin/python3
import re 
import json
import threading 
import time 
import queue
from os import path
from filelock import FileLock

class BANK_SERVER:

    def __init__(self):
        self.q     = queue.Queue(10)
        self.event = threading.Event()
        self.state = True
        t1 = threading.Thread(target = self.write_to)
        t1.start() 
        self.thread_count = 0

    def create_acc(self):
        create={}
        create1=[]
        acc_nos_list = []
        list_of_acc_no = []
        
        if not path.exists("bank_store.json"):
            with open("bank_store.json","w") as write:
                json.dump(acc_nos_list,write)
        

        if not path.exists("account_number_list.json"):
            with open("account_number_list","w") as write:
                json.dump(list_of_acc_no,write)
        
        self.acc_no=input("acc no:")
        if re.match("^322\d{8}",self.acc_no):

            with open("account_number_list","r") as read:
                details_of_acc_nos = json.load(read)

            details_of_acc_nos.append(self.acc_no)

            with open("account_number_list","w") as write:
                json.dump(details_of_acc_nos,write)
            
            self.holder_name=input("enter your name:")
            if re.match("[A-Z]\s[A-Z][a-z]\D+",self.holder_name):
                self.mobile_num=input("enter mobile number:")
                if re.match("9790|8248\d{6}",self.mobile_num):
                    self.email=input("enter mail id:")
                    if re.match("[a-z][a-z0-9]+[@][a-z]+.com",self.email):
                        self.acc_type=input("enter account type:")
                        self.init_deposit=int(input("enter initial deposit amount:"))
                        self.DOB=input("enter date of birth as dd/mm/yyyy:")
                        self.addr=input("enter your address:")

                        create["acc_no"]=self.acc_no
                        create["holder_name"]=self.holder_name
                        create["mobile_num"]=self.mobile_num
                        create["email"]=self.email
                        create["acc_type"]=self.acc_type
                        create["init_deposit"]=self.init_deposit
                        create["DOB"]=self.DOB
                        create["addr"]=self.addr

                        print(create)
                            

                        with open("bank_store.json","r") as store:
                            acc_details=json.load(store)
                        acc_details.append(create)
                        #print("acc_details:\n",acc_details)

                        with open("bank_store.json","w") as store:
                            json.dump(acc_details,store)
                    else:
                        print("please enter valid email")
                else:
                    print("please enter 10 digits mobile number")
            else:
                print("enter initial with name")
        else:
            print("please enter 11 digit currect acc number")
        


    def deposit(self):
        acc1_no="32209876543"#input("enter your acc number:")
        self.read_to()
        for acc in self.acc_details:
            if acc["acc_no"] == acc1_no:
                amount=1000#int(input("enter the amount:"))
                acc["init_deposit"]+=amount
        self.q.put(self.acc_details)
        self.event.set()

    def withdraw(self):
        acc1_no="32209876543"#input("enter your acc number:")
        self.read_to()
        for acc in self.acc_details:
            if acc["acc_no"] == acc1_no:
 
                amount=100#int(input("enter withdraw amount:"))
                acc["init_deposit"]-=amount
        self.q.put(self.acc_details)
        self.event.set()

    def user(self):
        user_name="nishavenkatesan1998"#input("enter the user name :")
        if user_name=="nishavenkatesan1998":
            passwrd="Nisha@1998"#input("enter password :")
            if passwrd=="Nisha@1998":
                self.create_acc()
            else:
                print("pls enter crt password")
        else:
            print("invalid user name")

    def read_to(self):
        with FileLock("bank_store.json"+".lock"):
          with open("bank_store.json","r") as store:
            self.acc_details=json.load(store)


    def write_to(self):
        self.count =0
        while self.state:
            self.event.wait()
            self.count+=1
            rcv_data=self.q.get()
            print("receive data:",rcv_data)
            with FileLock("bank_store.json"+".lock"):
                with open("bank_store.json","w") as store:
                    json.dump(rcv_data,store)
            self.event.clear()
            if self.count == self.thread_count:
                break


    def exit(self):
        if self.count == self.thread_count:
           self.state =False

obj=BANK_SERVER()

TD1 = threading.Thread(target = obj.deposit)
TD1.start()
obj.thread_count+=1
TD2 = threading.Thread(target = obj.withdraw)
TD2.start() 
obj.thread_count+=1
TD5 = threading.Thread(target = obj.deposit)
TD5.start()
obj.thread_count+=1
obj.exit()

