#!/usr/bin/python3
import re
'''string = "Emma loves \n Python"
check = re.search(r".",string)
print(check.group())'''

'''string = "Emma loves \n Python"
check = re.search(r".+",string)
print(check.group())'''


string = "Emma loves \n Python"
check = re.search(r".+",string,re.DOTALL or re.s)
print(check.group())


