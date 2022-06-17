#!/usr/bin/python3

import json
from os import path

lst = []
if not path.exists("nisha.json"):
    with open("nisha.json","w") as nisha:
        json.dump(lst,nisha)

data="hello"

with open("nisha.json","r") as read:
    data1 = json.load(read)
    print(data1)
with open("nisha.json","w") as write:
    print(data2)
    data2 = json.dump(data,write)
    print(data2)
