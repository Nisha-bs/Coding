#!/usr/bin/python3

grid = [
  ["0","0","0","0","0","0","0"],
  ["0","1","1","1","0","0","0"],
  ["0","0","1","0","1","0","0"],
  ["0","1","0","0","0","0","0"],
  ["0","0","0","0","1","0","0"],
  ["0","0","0","0","0","0","0"]
]
count = 0
'''
for index1 in range(1,len(grid)-1):
    for index2 in range(1,len(grid[0])-1):
        if grid[index1][index2] == "1":
            if grid[index1][index2+1] == "0" and grid[index1][index2 - 1] == "0" and grid[index1 + 1][index2] == "0" and grid[index1 - 1][index2] == "0":
                count += 1
                #print(count)
            else:
                continue
        else:
            continue
print(count)
'''

for index1 in range(1,len(grid)-1):
    for index2 in range(1,len(grid[0])-1):
        if grid[index1][index2] == "1":
            result = int(grid[index1][index2+1]) + int(grid[index1][index2 - 1]) + int(grid[index1 + 1][index2]) + int(grid[index1 - 1][index2])
            print(result, type(result))
            if result == 1:
                count += 1
            else:
                continue
        else:
            continue
print(count)

