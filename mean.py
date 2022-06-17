#!/usr/bin/python3


matrix = [[1, 1, 1], [0, 0, 0], [1, 0, 1]]
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

'''
while True:
    length_of_row = len(result)
    length_of_col = len(result[0])
    print("length_of_row length_of_col", length_of_row, length_of_col)
    print(len(result))
    for i in range(len(result)-1):
        for j in range(len(result)+1):
            final_add = result[i][j] + result[i+1][j] + result[i][j+1] + result[i+1][j+1]
            result[i][j] = final_add
    print("r", result)
   ''' '''
    final_r_len = (length_of_row - 2) + 1
    final_c_len = (length_of_col - 2) + 1
    
    result = []
    for i in range(final_r_len):
        rows = []
        for j in range(final_c_len):
            rows.append(0)
            result.append(rows)
    #print("result", result)

    if len(result) == 1:
        break
print(result)
'''
             

