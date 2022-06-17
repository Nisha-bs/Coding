#!/usr/bin/python3

import os
import subprocess as sp

name = input("enter name :")
output = sp.getoutput('locate ' + name)
print(output)

#store = output.split('/')
#print(store)

store = output.split(name)
print(store)

os.chdir(store[0])


'''for direc in range(1, len(store)-1):
    sp.getoutput('cd ' + store[direc])

sp.getoutput('vi interview.py')
#sp.getoutput('vi ' + store[len(store)-1])
'''
