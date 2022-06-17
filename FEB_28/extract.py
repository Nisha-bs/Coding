#extract values between quotation marks of a string.

#!/usr/bin/python3
import re
text1='"python","PHP","Java"'
#print(text1)
#str1=text1.split(",")
str1=re.findall(r'"(.*?)"',text1)
print(str1)


