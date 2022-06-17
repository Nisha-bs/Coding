#!/usr/bin/python3
import re 
import json
import threading 
import time 
import queue
from os import path

class BANK_SERVER:
    def create_acc(self):
        create={}
        create1={}
        list1=[{'acc_no':[]}]
        
        if not path.exists('pen.json'):
            with open("pen.json","w") as write:
                json.dump(list1,write)
        
        self.acc_no=input("enter acc no:")
        if re.match("^322\d{8}",self.acc_no):
            with open("pen.json","r") as gud:
                list1=json.load(gud)
                for x in range(len(list1)):
                    print("list1:\n",x[0])

                #for x in list1:
                 #   if x["acc_nos"]:
                  #      print(x["acc_nos"])
                   # else:
                    #    print("no")
                with open("pen.json","w") as gud:
                    json.dump(list1,gud)
                #list1.append(create1)
                #print("details:",list1)
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

                            #print(create)
                            

                            with open("bank_store.json","r") as store:
                                acc_details=json.load(store)
                            acc_details.append(create)
                            #print("acc_details:\n",acc_details)

                            with open("bank_store.json","w") as store:
                                json.dump(acc_details,store)
                            self.main()
                        else:
                            print("please enter valid email")
                    else:
                        print("please enter 10 digits mobile number")
                else:
                    print("enter initial with name")
            #else:
             #   print("acc no already exist")
              #  self.create_acc()
        else:
            print("please enter 11 digit currect acc number")
        


    def deposit(self):
        acc1_no=input("enter your acc number:")
        self.read_to()
        for acc in self.acc_details:
            print(acc["acc_no"])
            if acc["acc_no"] == acc1_no:
                amount=int(input("enter the amount:"))
                acc["init_deposit"]+=amount
        self.write_to()



    def withdraw(self):
        acc1_no=input("enter your acc number:")
        self.read_to()
        for acc in self.acc_details:
            if acc["acc_no"] == acc1_no:
                amount=int(input("enter withdraw amount:"))
                acc["init_deposit"]-=amount
        self.write_to()

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


    def main(self):
        print("1.create account\n2.deposit amount\n3.withdraw amount\n4.exit")
        ch=int(input("enter:"))
        if ch==1:
            obj.user()
        elif ch==2:
            self.deposit()
        elif ch==3:
            self.withdraw()
        else:
            exit()


    def read_to(self):

        with open("bank_store.json","r") as store:
            self.acc_details=json.load(store)

    def write_to(self):
        
        with open("bank_store.json","w") as store:
            json.dump(self.acc_details,store)




obj=BANK_SERVER()
obj.main()

