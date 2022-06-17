#!/usr/bin/python3

numRows = 2
res = [[1],[1,1]]

if numRows == 1:
    print([res[0]])
elif numRows == 2:
    print(res)
else:
    for i in range(2,numRows):
        temp = [1]
        for j in range(1,len(res[i-1])):
            temp.append(res[i-1][j-1] + res[i-1][j])
        temp.append(1)
        res.append(temp)

    print(res)
