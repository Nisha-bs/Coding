#!/usr/bin/python3

n = 6

for i in range(0, n):
    for j in range(i,-1,-1):
        print(2**j, end = "")
    print("")


for i in range(n,-1,-1):
    for j in range(1,i):
        print(j,end="")
        if j < i-1:
            print(end="*")
    print("")

def matrix(length): 
    for  i in range(length-1):
        add = 0
        add_list = []
        for j in range(length):
            print(grid[i][j])
            add += grid[i][j]
            add_list.append(add)
        print("")
    print(add_list)
    for i in range(len(add_list)-1):
        if add_list[i] == add_list[i+1]:
            continue
        else:
            length -= 1
            matrix(length)
grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
length = len(grid) + 1
matrix(length)
