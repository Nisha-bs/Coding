#!/usr/bin/python3

matrix = [[0, 0, 1],[0, 0, 1],[0, 0, 1]]
length = len(matrix)
print("matrix ",matrix)
list1 = []
for row in matrix:
    row_length = len(row)
    #print(row_length)
    for inner_row in range(row_length+1):
        if inner_row == 0:
            row.insert(0,1)
        elif inner_row == row_length:
            row.append(1)
for pad in range(length+2):
    list1.append(1)
matrix.insert(0,list1)
matrix.append(list1)
print("padded_matrix ",matrix)
padded_matrix = len(matrix)

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(1, padded_matrix-1):
    for j in range(1, padded_matrix-1):
            if matrix[i][j] == 1 and matrix[i+1][j] == 1:
                if matrix[i][j+1] == 1 and matrix[i+1][j+1] == 1: 
                    result[i-1][j-1] = 1
                else:
                    result[i-1][j-1] = 0
            else:
                result[i-1][j-1] = 0

print("result_matrix ",result)
