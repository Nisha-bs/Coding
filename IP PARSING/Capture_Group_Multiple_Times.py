#!/usr/bin/python3
import re
target_string = "The price of ice-creams PINEAPPLE 20 MANGO 30 CHOCOLATE 40"
pattern = re.compile(r"([A-Z]+).([\d]+)")
match = re.findall(pattern,target_string)
print(match)
for match in pattern.finditer(target_string):
    print(match.group(0))
