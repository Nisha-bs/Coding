#!/usr/bin//python3

import itertools

input_list = [1,-2,1,-3,2,]
com_list = itertools.combinations(input_list,3)
for val_list in com_list:
    result = 0
    for value in val_list:
        result = result + value 
    if result == 0:
        print(val_list)
    else:
        pass
