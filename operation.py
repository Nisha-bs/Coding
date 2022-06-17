#!/usr/bin/python3

operators_operands = ["6","2","1","+","/","1","-","1","*"]
operators_operands1 = operators_operands.copy()
index = 0 
while len(operators_operands)>1:
    #for index,operands in enumerate(operators_operands1[:]):
    operands = operators_operands[index]
    if operands == "+":
        result = int(operators_operands[index-2]) + int(operators_operands[index-1])
        operators_operands.insert(index+1,str(result))
        del operators_operands[index-2:index+1]
        index = 0
        print(operators_operands)
    elif operands == "-":
        print('eeee1')
        result = float(operators_operands[index-2]) - float(operators_operands[index-1])
        operators_operands.insert(index+1,str(result))
        del operators_operands[index-2:index+1]
        index = 0
        print('eeee1')
        print(operators_operands)
    elif operands == "*":
        print('eeee1')
        result = float(operators_operands[index-2]) * float(operators_operands[index-1])
        operators_operands.insert(index+1,str(result))
        del operators_operands[index-2:index+1]
        index = 0
        print(operators_operands)
    elif operands == "/":
        result = int(operators_operands[index-2]) / int(operators_operands[index-1])
        operators_operands.insert(index+1,str(result))
        del operators_operands[index-2:index+1]
        index = 0
        print(operators_operands)
    else:
        index += 1
print(operators_operands) 

        
