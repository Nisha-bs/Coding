#!/usr/bin/python3

import os
import re

Process_name = input("enter process name")
processes = os.system('ps -e | grep ' + Process_name)


value = str(processes)
print(value)

list1 = re.split("\s", value)
print(list1)
