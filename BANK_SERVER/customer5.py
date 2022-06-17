#!/usr/bin/python3
import re 
import json
import threading 
import time 
import queue
q=queue.Queue(10)
class BANK_SERVER:
    def create_acc(self):
        acc_list=["32205643678"]
        create={}
        self.acc_no=input("enter the acc number:")
        if re.match("^322\d{8}",self.acc_no):
            if self.acc_no not in acc_list:
                acc_list.append(self.acc_no)
                print(acc_list)
                self.holder_name=input("enter your name:")
                if re.match("[A-Z]\s[A-Z][a-z]\D+",self.holder_name):
                    self.mobile_num=input("enter mobile number:")
                    if re.match("9790|8248\d{6}",self.mobile_num):
                        self.email=input("enter mail id:")
                        if re.match("[a-z][a-z0-9]+[@][a-z]+.com",self.email):
                            self.acc_type=input("enter account type:")
                            self.init_deposit=int(input("enter initial payment:"))
                            self.DOB=input("enter date of birth as dd/mm/yyy:")
                            self.addr=input("enter your address:")
                        else:
                            print("please enter valid email")
                    else:
                        print("please enter 10 digits mobile number")
                else:
                    print("enter initial with name")
            else:
                print("acc number already exist")
        else:
            print("please enter 11 digit currect acc number")

        create["acc_no"]       = self.acc_no
        create["holder_name"]  = self.holder_name
        create["mobile_num"]   = self.mobile_num
        create["email"]        = self.email
        create["acc_type"]     = self.acc_type
        create["init_deposit"] = self.init_deposit
        create["DOB"]          = self.DOB
        create["addr"]         = self.addr

        print(create)


        with open("bank_store.json","r") as store:
            acc_details=json.load(store)
        acc_details.append(create)
        print("acc_details:\n",acc_details)

        with open("bank_store.json","w") as store:
             json.dump(acc_details,store)
        self.main()



    def deposit(self,amount):
        acc1_no=32207654678#input("enter your acc number:")
        self.read_to()
        for acc in self.acc_details:
            print(acc["acc_no"])
            if acc["acc_no"] == acc1_no:
                #amount=int(input("enter the amount:"))
                acc["init_deposit"]+=amount

        data={}
        data["acc_details"]=self.acc_details
        q.put(data)

        self.write_to()
        self.main()

    def withdraw(self,amount):
        acc1_no=input("enter your acc number:")
        self.read_to()
        for acc in self.acc_details:
            print(acc)
            if acc["acc_no"] == acc1_no:
                #amount=int(input("enter withdraw amount:"))
                acc["init_deposit"]-=amount
        data={}
        data["acc_details"]=self.acc_details
        q.put(data)

        self.write_to()
        self.main()

    def user(self):
        user_name=input("enter the user name :")
        if user_name=="nishavenkatesan1998":
            passwrd=input("enter password :")
            if passwrd=="Nisha@1998":
                self.create_acc()
            else:
                print("pls enter crt password")
        else:
            print("invalid user name")

    
    def read_to(self):

        with open("bank_store.json","r") as store:
            self.acc_details=json.load(store)

    def write_to(self):
        while True:
            if not q.empty():
                rcv_data=q.get()
                print("receive data:",rcv_data)
        with open("bank_store.json","w") as store:
            json.dump(self.acc_details,store)

    def main(self):
        print("1.create account\n2.deposit amount\n3.withdraw amount\n4.exit")
        ch=int(input("enter:"))
        if ch==1:
            self.user()
        elif ch==2:
            self.deposit(2000)
        elif ch==3:
            self.withdraw(1000)
        else:
            exit()

obj=BANK_SERVER()
obj.main()
TD1=threading.Thread(target=obj.write_to)
TD2=threading.Thread(target=obj.write_to)
TD1.start()
TD2.start()
#TD2.join()
