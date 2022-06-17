#!/usr/bin/python3
import subprocess as sp
x=sp.getoutput('netstat -ua')
print(x)


