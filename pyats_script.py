#!/usr/bin/python3

import yaml
from yaml.loader import SafeLoader

with open('confg.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
#print(data)

def iter_file(data):
    for routers,router in data.items():
        for key1,value1 in router.items():
            interface=key1
    return key1,value1
def ipv4_6(key1,value1):         
            ipv4addr = value1["ipv4addr"]
            ipv6addr = value1["ipv6addr"]
            subnet_mask = value1["subnetmask"]
            script = f"interface {interface} \n ipv4 address {ipv4addr} {subnet_mask}\n ipv6 address {ipv6addr} \n no shut "
            print(script)
def ipv4():
            ipv4addr = value1["ipv4addr"]
            script = f"interface {interface} \n ipv4 address {ipv4addr} {subnet_mask} \n no shut"
            print(script)
def ipv6():
            ipv6addr = value1["ipv6addr"]
            script = f"interface {interface} \n ipv6 address {ipv6addr} \n no shut"
            print(script)

def main(data):
        if "ipv4addr" in value1.keys() and "ipv6addr" in value1.keys():
            ipv4_6(key1,value1)
        elif "ipv4addr" in value1.keys():
            ipv4()
        elif "ipv6addr" in value1.keys():
            ipv6()
iter_file(data)
main(data)
