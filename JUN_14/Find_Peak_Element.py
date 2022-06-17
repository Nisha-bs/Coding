#!/usr/bin/python3

nums = [1,2,4,1]
peak = 0
for index, number in enumerate(nums):
    #print(index)
    if peak < number:
        peak = number
    else:
        continue
    print(peak,index)
