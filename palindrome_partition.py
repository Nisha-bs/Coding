#!/usr/bin/python3
s = "aab"
list1 = []
for index in range(len(s)):
    for index1 in range(1,len(s)+1):
        string = s[index:index1]
        print("string",string)
        string_reverse = string[::-1]
        #print("string_reverse",string_reverse)
        if string == string_reverse:
            list1.append(string)
        else:
            pass
list1 = list(filter(None, list1))
print(list1)
