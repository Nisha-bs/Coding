#!/usr/bin/python3

string = f'''Port   VRF          Status IP Address                              Speed    MTU
Ethernet Interface     VLAN    Type Mode   Status  Reason                   Speed     Port
Eth1/1        1       eth  routed up      none                       1000(D) --
Eth1/2        --      eth  routed up      none                       1000(D) --
Eth1/3        --      eth  routed up      none                       1000(D) --'''

split_line = string.split("\n")

dict_string = {}
list1 = [] 
for line in split_line:
    word = line.split()
    list1.append(word)
print(list1)

for lst in list1:
    for wrd in lst:
        dict_string[wrd] = dict()
print(dict_string)





