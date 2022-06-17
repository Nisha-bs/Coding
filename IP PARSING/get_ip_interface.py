#!/usr/bin/python3
txt="""enp1s0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether f4:39:09:dd:41:f0  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 14841  bytes 1516181 (1.5 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 14841  bytes 1516181 (1.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp2s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.124  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::affb:6f97:cbc7:82b9  prefixlen 64  scopeid 0x20<link>
        ether d0:c5:d3:7a:f0:35  txqueuelen 1000  (Ethernet)
        RX packets 264264  bytes 107263557 (107.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 90780  bytes 18336466 (18.3 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0"""
		
new_dict={}
import re
lines=txt.split("\n")

txt_1,txt_2,txt_3="","",""
ln=""
for line in range(len(lines)):
    #print(lines[line])
    if "lo:" in lines[line]:
        #print(lines[line])
        for nxt in range(line,len(lines)):
            #print(lines[nxt])
            if "wlp2s0:" in lines[nxt]:
                print(lines[nxt])
                for last in range(nxt,len(lines)):
                    txt_3+="".join(lines[last])
                    print(txt_3)
                break
            else:
                txt_2+="".join(lines[nxt])
        break        
    else:
        txt_1+="".join(lines[line])
    
txt_1_list,txt_2_list,txt_3_list = txt_1.split(),txt_2.split(),txt_3.split()
key1,key2,key3 = txt_1_list[0],txt_2_list[0],txt_3_list[0]


regex=r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
txt_1val=re.findall(regex,txt_1)
txt_2val=re.findall(regex,txt_2)
txt_3val=re.findall(regex,txt_3)

new_dict[key1]=txt_1val
new_dict[key2]=txt_2val
new_dict[key3]=txt_3val

for intf,ip in new_dict.items():
    print(intf,ip)
