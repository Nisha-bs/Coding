#!/usr/bin/python3
import re
target_string = "Emma is a Python developer and her salary is 5000$ \nEmma also knows ML and AI"

'''match = re.search(r"^\w{4}",target_string)
print(match.group())'''

match = re.findall(r"^\w{4}",target_string, re.M)
print(match)

