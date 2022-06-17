#!/usr/bin/python3
import re
str1="hello hiii nisha"
#out=re.sub(" +"," ",str1)
out=re.sub("\s+","",str1)
print(out)


#remove all except alphanumeric
import re
str1="\\**hello hiii nisha\\-12."
out=re.sub("\W+","",str1)
#out=re.sub("[\W_]+","",str1)
print(out)
