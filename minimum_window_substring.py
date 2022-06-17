#!/usr/bin/python3
s = "ADOBECODEBANC"
t = "ABC"
length = len(t)
#print(length)

#string = ""
i = 1
p1=0
p2=0
substring_list = []
for index, letter in enumerate(s):
    i = 1
    #print(index)
    if letter in t:
        string = s[p2:p2+index]
    #print(string)
        for alphabetic in t:
        #print(i)
            if alphabetic in string and i == length:
                #print(i)
                substring_list.append(string)
                #print("sub",substring_list)
                i =1 
                p2=index
                break
            elif alphabetic in string and i < length:
                #print("string",string)
                i += 1
            else:
                continue
    else:
        continue
print(min((word for word in substring_list), key =len))
