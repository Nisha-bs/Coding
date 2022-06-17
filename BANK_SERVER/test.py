#!/usr/bin/env python3

import json
import threading
from queue import Queue
from filelock import FileLock

q     = Queue()
w_q     = Queue()
event = threading.Event()
w_event = threading.Event()


def write_to_file():
    w_event.wait()
    data = w_q.get()
    with FileLock("test.json"+".lock"):
        with open("test.json", "w") as file:
            json.dump(data,file)
    w_event.clear()

def deposit():

   while True:

       
       event.wait()
       new_data = q.get()
       if new_data['id'] == 0:
          with FileLock("test.json"+".lock") :
             with open("test.json", "r") as file:
                  data = json.load(file)
          data['amount'] +=new_data['amount']
          w_q.put(data)
          w_event.set()     
          event.clear()

def withdraw():

   while True:

       event.wait()
       new_data = q.get()
       if new_data['id'] == 1:
          with FileLock("test.json"+".lock") :
             with open("test.json", "r") as file:
                  data = json.load(file)
          data['amount'] -=new_data['amount']
          w_q.put(data)
          w_event.set()     
          event.clear()

def comman_q():

   while True:
       data = {}
       id             = int(input("deposit[0]/withdraw[1] >"))
       amount         =  int(input("amount >"))
       data['id']     = id
       data['amount'] = amount

       q.put(data)
       event.set()


t1 = threading.Thread(target=deposit)
t2 = threading.Thread(target=withdraw)
t3 = threading.Thread(target=comman_q)
t4 = threading.Thread(target=write_to_file)


t4.start()
t1.start()
t2.start()
t3.start()
