#!/usr/bin/python3

s = "[123,[456,[789]]]"

num = s.split("[]")
print(num)
string = ""
for val in num:
    #print(val)
    string += val
#print(string)

