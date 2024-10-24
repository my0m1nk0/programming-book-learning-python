input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

if(operator == "+"):
    result = input1 + input2
elif(operator == "-"):
    result = input1 - input2
elif(operator == "*"):
    result = input1 * input2
elif(operator == "/"):
    result = input1 / input2
elif(operator == "%"):
    result = input1 % input2                

# result = input1 + input2
# result = input1 - input2 
# result = input1 * input2
# result = input1 / input2
# result = input1 % input2

print("The two numbers ",input1 ,operator, input2 ,"is :", result)
