#!/usr/bin/python3
import subprocess as sp
import re
string=sp.getoutput("ip add")
print(string)
split=re.split("\d: \w+:",string)
print(split)
