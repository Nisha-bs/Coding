#!/usr/bin/python3
import re
string="hello_nisha"
str1=string.split("_")
#print(str1)
list1=[]
list2=[]
list3=[]
str2=""
for word in str1:
    
    list1.append(word[0])
    list2.append(word[1:len(word)])
    '''print("list1",list1)
    print("list2",list2)'''
    for first in  range(0,len(list1)):
        for second in range(0,len(list2)):
            if first==second:
                #print(first,second)
                list3.append((list1[first].upper())+(list2[second]))
                print(list3)
                for i in list3:
                    str2=str2+i
print(str2)


