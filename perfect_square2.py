#!/usr/bin/python3
import itertools 
'''
list1= []
def find(s, ind, n, answer): 

    if(ind == n): 
        list1.append(answer)
        print(answer) 
        print(list1)
        return 
         
    find(s, ind+1, n, answer+s[ind]) 
    find(s, ind+1, n, answer) 

    add = 0
    for val in list1:
        add = 0
        for digit in val:
            value = (int(digit))
            #print(type(value))
            add =add + value
            print(add)
            if add == n:
                print(add)


 
s = ["4","9","16"] 
find(s, 0, len(s), "")
'''

a_list = ["4","9","16"]
all_combinations = []
for r in range(len(a_list) + 1):
#Add all combinations of `a_list` to `all_combinations`

    combinations_object = itertools.combinations(a_list, r)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list

print(all_combinations)

n =20
for i in all_combinations:
    print(i)
    add = 0
    count = 0
    for j in i:
        #print(j)
        add += int(j)
        count += 1
        print("add",add)
        if add == n:
            print("count",count)
        else:
            pass


for val in a_list:
    i = 1
    if val ** i == n:
        print(i)
    elif val ** i != n:
        i += 1


