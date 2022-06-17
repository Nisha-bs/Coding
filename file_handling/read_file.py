#!/usr/bin/python3

#o=open("text_file.txt","rt")
#o=open("D:\\Home\PYTHON\file_handling\text_file.txt","rt")?
#print(o.read(2))#read 1st 2 characters
#print(o.readline(6))

'''for x in o:
    print(x)'''

'''
o=open("text_file.txt","w")
print(o.write("goo"))
o.close()

o=open("text_file.txt","r")
print(o.read())'''
import os 
try:
    os.remove("text_file.txt")
except:
    print("exceptipn error")
else:
    print("gud bye")


