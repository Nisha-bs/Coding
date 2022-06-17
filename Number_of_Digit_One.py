#!/usr/bin/python3

n = 16
'''
count = 0 
for i in range(n+1):
    val = str(i)
    for j in range(len(val)):
        #print(i)
        if val[j] == "1":
            count += 1
        else:
            continue
print(count)
'''
'''
add = "0"
for i in range(n+1):
    add += str(i)
print(add.count("1"))
''''''
add = 0
for i in range(n+1):
    add += str(i).count("1")
print(add)'''

print(sum([str(i).count("1") for i in range(n+1)]))

