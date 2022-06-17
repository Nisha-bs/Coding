#!/usr/bin/python3

value = 9

square_root = (value)**(1/2)
print(int(square_root))

for perfect_squares in range(1, int(square_root)+1):
    print(perfect_squares*perfect_squares,end = " ")
