#!/usr/bin/python3
import queue 
import threading
import json

q1 = queue.Queue(10)

event = threading.Event()


def write_to_json():

    while True:

        event.wait()
        data = q1.get()
        with open("test.json","w") as files:
             json.dump(data,files) 
        print(f"data : {data} successfully added\n")

def data_to_queue(msg):

    with open("test.json","r") as files:
        data = json.load(files)
    data.append(msg)
    q1.put(data)
    event.set()
    print(f"data : {data} successfully send\n")

t1 = threading.Thread(target=write_to_json,daemon=True)
t1.start()
data = {"Name":"Jeyendran K"}
data_to_queue(data)

