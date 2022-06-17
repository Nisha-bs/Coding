#!/usr/bin/python3
import queue
import time
import threading
q=queue.Queue(1024)

def thrd1():
    account_no = input("acc_no > ")
    data = {}
    data['aac_no'] = account_no
    data['file_name'] = "bank_store.json"
    q.put(data)
def thrd2():
    while True:
       #if not q.empty():
           recv_data = q.get()
           print(f"received data: {recv_data}")
           print(type(recv_data))
thrd1()
TD1=threading.Thread(target=thrd2, daemon=True)
TD1.start()
time.sleep(2)
