#!/usr/bin/python3

import json
from os import path
import time
d={1:'nish'}


if not path.exists('test1.json'):
    with open('test1.json','w') as write:
        list1 = json.dump(d,write)
        print(list1)


with open('test1.json','r') as read:
    load1 = json.load(read)
    print(load1)
with open('test1.json','w') as write:
    list1 = json.dump(d,write)

    print("hi")
