#!/usr/bin/python3
import re
string="acc"
check=re.search("^ab*$",string)
if  bool(check):
    print("true")
else:
    print("else")
