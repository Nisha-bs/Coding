#!/usr/bin/python3

triangle = [[2]]
add = 0

if len(triangle) == 1:
    print(triangle)
else:
    for rows in triangle:
        min_val = min(rows)
        add += min_val
    print(add)
    if len(triangle) == 1:
        print(triangle)

