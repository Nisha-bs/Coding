#!/usr/bin/python3

import subprocess as sp
import re
import os

Process_name = input("enter process name")
processes = sp.getoutput('ps -e | grep ' + Process_name)
#print(processes)

lines = processes.split("\n")
print(lines)

list2 = []
for line in lines:
    list1 = line.split()
    list2.append(list1)
print(list2)

PID_list = []
for PID in list2:
    #PID_list.append(PID[0])
    process_id = 'kill ' + str(PID[0])
    #os.system(process_id)
    sp.getoutput(process_id)
#print(PID_list)


