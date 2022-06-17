#!/usr/bin/python3

def padding(matrix):

    #matrix = [[0, 0, 1],[0, 0, 1],[0, 0, 1]]
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
    return result

def mean(matrix):

    #matrix = [[1, 1, 1], [0, 0, 0], [1, 0, 1]]
    row_length = len(matrix)
    col_length = len(matrix[0])
    row1_length = int(input("enter row length"))
    col1_length = int(input("enter the col length"))
    result_row_matrix = (row_length - row1_length) + 1
    result_col_matrix = (col_length - col1_length) + 1

    result = []
    for i in range(result_row_matrix):
        rows = []
        for j in range(result_col_matrix):
            rows.append(0)
        result.append(rows)
    #print(result)
    #print(result_row_matrix, result_col_matrix)

    value = row1_length * col1_length
    for row in range(len(matrix)-1):
        #print(matrix[row])
        for col in range(result_col_matrix):
            #print(matrix[row][col])
            add1 = matrix[row][col] + matrix[row+1][col]
            #print("add1", add1)
            add2 = matrix[row][col+1] + matrix[row+1][col+1]
            #print("add2", add2)
            add = (add1 + add2) / value
            #print("add", add)
            result[row][col] = add
    print(result)

#matrix = input("enter matrix")
mean(padding([[1,1,1],[0,0,0],[1,0,1]]))




