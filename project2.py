operand = input("number 1 : ")
operand2 = input("number 2 : ")
sign = input("Sing: ")
result = 0
if sign == '+':
    result = float(operand) + float(operand2)           # or result = operand + operand2    (it`s the same result`)
elif sign == '-':
    result = float(operand) - float(operand2)           # or result = operand - operand2    (it`s the same result`)
elif sign == '/':
    result = float(operand) / float(operand2)         
elif sign == '*':
    result = float(operand) * float(operand2)

print(result)