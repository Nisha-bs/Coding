'''Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 192.168.0.113:48454     34.120.5.221:443        ESTABLISHED
tcp        0      0 192.168.0.113:41220     142.250.182.100:443     TIME_WAIT  
tcp        0      0 192.168.0.113:40360     34.120.208.123:443      ESTABLISHED
tcp        0      0 192.168.0.113:46910     35.82.230.35:443        ESTABLISHED
'''
#!/usr/bin/python3
import re
import subprocess as sp

string=sp.getoutput("netstat -tn")
print(string)
pattern=re.findall("([12]{1,3})([9012]{1,3})([23]{1,3})")
