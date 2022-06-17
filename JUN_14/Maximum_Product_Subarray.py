#!/usr/bin/python3

nums = [-1, 0 ,-2]
result_list = []
for subarray in range(1, len(nums)+1):
    array = nums[:subarray]
    mul = 1
    print(array)
    for val in array:
        mul = mul * val
    result_list.append(mul)
print("final_llist",  result_list)
maximum_val = max(result_list)
print(maximum_val)
