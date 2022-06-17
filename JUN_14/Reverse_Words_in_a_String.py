#!/usr/bin/python3

s = "the sky is blue"
list1 = []
split_list = s.split()
print(split_list)
final_string = " "
for word in range(len(split_list)-1,-1,-1):
    final_string += split_list[word]
print(final_string)
