#!/usr/bin/python3
import re
'''string="hello nisha how are you nisha"
string1="nisha"
matched=re.search(string1,string)
pos=matched.start()
print(pos)
'''

'''
for match in re.finditer(string1,string):
    pos=match.start()
    pos=match.end()
    print(pos)
'''
'''
string="hello nisha are u 18 or 20"
for match in re.finditer("\d+",string):
    #match.group(0)
    print (match.start())
    '''
'''string="road accident is append not in my area"
change=re.sub("road","rd",string)
print(change)
'''
'''
string="i am sitting in my office, for some purpose."
rep=re.sub("[ ,.]",";",string)
print(rep)
'''
'''
string="i  am sitting  in  my  office, for  some  purpose."
rep=re.sub("[ ,.]", ";", string, 2)
print(rep)
'''
'''
string="i am sitting in my office, for some purpose."
find=re.findall(r"\b\w{2}\b",string)
print(find)
'''
'''
string="i am sitting in my office, for some purpose."
find=re.findall(r"\b\w{3,5}\b",string)
print(find)
'''

string="i am sitting in my office, for some purpose."
find=re.findall(r"\b\w{3,}\b",string)
print(find)
