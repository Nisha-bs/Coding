#!/usr/bin/python3

nums = [9,12,5,10,14,3,10]
pivot = 10
list1 = []
list2 = []

for num in nums:
    if num < pivot:
        list1.append(num)
    else:
        list2.append(num)

lst = list1 + list2
print(lst)
