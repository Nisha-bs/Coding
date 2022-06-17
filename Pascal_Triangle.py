#!/usr/bin/python3
'''
def pascal(list1, add):
    i = 0
    for i in range(len(list1)):
        add = list1[0] + list1[i+1]
        list1.insert(i, add)
        i += 1
        print(list1)
        if len(list1)== 10:
            break
    pascal(list1, 1)

pascal([1, 2], 1)
'''

rows = 3

# creating a pascal triangle of required siz
pstri = [[1] * r for r in range(1,rows+1)]
'''pstri = [[]]
for r in range(1, rows+1):
    pstri = [1] * r
print(pstri)'''
for i in range(2,rows):
    for j in range(1,i):
        pstri[i][j] = pstri[i-1][j] + pstri[i-1][j-1]
print(pstri)

