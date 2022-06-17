#!/usr/bin/python3
import re
'''date="21-03-1998"
change=re.sub('(\d{1,2})-(\d{1,2})-(\d{2,4})','\\3-\\2-\\1',date)
print(change)
'''
ip="192.168.0.1"
change=re.sub('(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})','\\4.\\3.\\2.\\1',ip)
print(change)

