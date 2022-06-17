#!/usr/bin/python3

def minimum_length_array():
    target = 7
    nums = [2,3,1,2,4,3]
    length_array = []
    if target in nums:
        print("1")
    else:
        j = 0
        for i in range(len(nums) + 1):
            for j in range(len(nums) + 1):
                subarray = nums[i:j]
                add = sum(subarray)
                if add == target:
                    length = len(subarray)
                    length_array.append(length)
    print(min(length_array))
minimum_length_array()
