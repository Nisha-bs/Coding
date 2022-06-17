#!/usr/bin/python3
import re
string="=@#+"
#string="nishahello"
check=re.search(r"[a-zA-Z0-9]",string)
print(bool(check))

