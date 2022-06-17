import subprocess as sp
import re
out_str=sp.getoutput("ipconfig")
res=re.search("IPv4.*\n",out_str)
print(res[0])
