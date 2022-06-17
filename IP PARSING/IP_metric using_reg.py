import subprocess as sp
import re
output=sp.getoutput("route print")
str=str(input("Enter the metric: "))
regex="[0-9]{1,3}\.[0-9]{1,3}\.[0-9][1,3}\.[0-9]{1,3}.*"+str
search_line=re.findall(regex,output)
for each_line in search_line:
    print(each_line)
# reg=re.search(regex,out)
# print(reg.group())
