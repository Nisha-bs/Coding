#!/usr/bin/python3

n = 13

value = n 

square_root = (value)**(1/2)
#print(int(square_root))
list1 = []
for perfect_squares in range(1, int(square_root)+1):
    square = perfect_squares*perfect_squares
    list1.append(square)
#print(list1)

rstl = 0
count = 0
for val in list1:
    rstl += val
    #print(rstl)
    count += 1
    if rstl == n:
        print("coount", count)
    elif rstl > n:
        i = 0
        if val < n:
            for i in range(n//2):
                rstl += list1[i]
                count = 1
                #print(rstl)
                if rstl == n:
                    print("cnt",count)
                elif rstl > n:
                    count = 0
                    i += 1
                    break
                else:
                    pass
    else:
        pass

