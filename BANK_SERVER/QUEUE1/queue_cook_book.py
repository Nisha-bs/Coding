#!/usr/bin/python3
import threading
import  queue
q=queue.Queue()
def run():
    data="nisha"
    q.put(data)
    return data
def compile(data):
    if not q.empty():
        print(q.get())

Th=threading.Thread(target=compile)
Th.start()
compile(data)
