#!/usr/bin/python3

row_size = 9
x = row_size
y = row_size

for j in range(row_size):
    for i in range(1,row_size*2):
        if i > x and i < y:
            print(" ", end="")
        else:
            print("*",end = "")
    x = x-1
    y = y+1
    print("")
