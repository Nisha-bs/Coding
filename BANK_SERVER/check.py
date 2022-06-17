#!/usr/bin/python3
import json
from os import path
create_list=[]
create2=[]
list1=[0]
create_dict = {} 
if not path.exists("pen1.json"):
    with open("pen1.json","w") as wri:
        json.dump(list1,wri)
new_acc_nos = input("new_acc no:")

with open("bank_store.json","r") as red:
    acc_details = json.load(red)
for i in acc_details:
        print(i)
        if new_acc_nos not in i["acc_no"]:
            print(i["acc_no"])
            '''create1.append(new_acc_nos)
            create_dict["new_acc_no"] = create1'''

            with open("pen1.json","r") as gud:
                list1 = json.load(gud)
                list1.append(create_list)


            with open("pen1.json","w") as gud:
                json.dump(create_dict,gud)

    else:
        print("exist")
    print("details:",create_dict)

