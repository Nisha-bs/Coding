#!/ur/bin/python3
import re
'''#string="abbb"
string="abc"
out=re.findall("a.+b",string)
print(out)
'''
#Matches a string that has an a followed by zero or one 'b'
#string="abc"
string="abbc"
out=re.findall("ab?",string)
print(out)


