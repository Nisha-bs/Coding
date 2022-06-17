#!/usr/bin/python3

import threading
import queue
import json
from os import path
from filelock import FileLock
q = queue.Queue()
event = threading.Event()


class three:
    
    
    data = {}

    if not path.exists("three_thredaing.json"):
        with open("three_threading.json","w") as write:
          json.dump(data,write)
    if not path.exists("users.json"):
        with open("users.json","w") as write:
          json.dump(data,write)
    
    def input_func(self):
        self.details = {}
        with open("three_threading.json","r") as read:
            json.load(read)
        self.account_number = int(input("enter the account number"))
        self.amount = int(input("enter the amount"))
        self.enter_id =int(input("enter the id"))
        self.details["account_number"] = self.account_number
        self.details["amount"] = self.amount
        self.details["enter_id"] = self.enter_id
        with open("three_threading.json","w") as write:
            json.dump(self.details,write)
        q.put(self.details)
        event.set()
    
    def deposit(self):
        with open("three_threading.json","r") as read:
            val = json.load(read)
        with open("users.json","r") as read:
            val1 = json.load(read)
        #with FileLock("users.json"+".lock"):
        if val["account_number"] == val1["acc_no"]:
            with open("users.json","r") as read:
                json.load(read)
            val1["amnt"] += val["amount"]
            with open("users.json","w") as write:
                json.dump(val1,write)
                print("finish")

    def withdraw(self):
        with open("three_threading.json","r") as read:
            val = json.load(read)
        with open("users.json","r") as read:
            val1 = json.load(read)
        if val["account_number"] == val1["acc_no"]:
            with FileLock("users.json"+".lock"):
                with open("users.json","r") as read:
                    json.load(read)
                val1["amnt"] -= val["amount"]
                with open("users.json","w") as write:
                    json.dump(val1,write)
                
    def queue_func(self):
    
        while True:
            event.wait()
            store = q.get()
            with open("three_threading.json","r") as read:
                details = json.load(read)
            if details["enter_id"] == 1:
                with open("three_threading.json","r") as read:
                    val = json.load(read)
                with open("users.json","r") as read:
                    val1 = json.load(read)
                #with FileLock("users.json"+".lock"):
                if val["account_number"] == val1["acc_no"]:
                    with open("users.json","r") as read:
                        json.load(read)
                    val1["amnt"] += val["amount"]
                    with open("users.json","w") as write:
                        json.dump(val1,write)

    
    def withdraw(self):

        while True:
            event.wait()
            store = q.get()
            with open("three_threading.json","r") as read:
                details = json.load(read)
            if details["enter_id"] == 1:
                with open("three_threading.json","r") as read:
                    val = json.load(read)
                with open("users.json","r") as read:
                    val1 = json.load(read)
                #with FileLock("users.json"+".lock"):
                if val["account_number"] == val1["acc_no"]:
                    with open("users.json","r") as read:
                        json.load(read)
                    val1["amnt"] -= val["amount"]
                    with open("users.json","w") as write:
                        json.dump(val1,write)







h = three()
h.input_func()
'''TD1 = threading.Thread(target = h.input_func, daemon = True)
TD1.start()'''
TD2 = threading.Thread(target = h.deposit)
TD2.start()
TD3 = threading.Thread(target = h.withdraw)
TD3.start()
TD4 = threading.Thread(target = h.queue_func)
TD4.start()
#TD1.join()
TD2.join()
TD3.join()
TD4.join()
