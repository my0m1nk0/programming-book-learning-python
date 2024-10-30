firstnum = input("Enter first number: ")
operator = input("Enter operator( + , -, * , /) :")
secondnum = input("Enter second number: ")
output = True 

try:
    firstnum = int(firstnum)
    secondnum = int(secondnum)
    
    if(operator == "+"):
        result = firstnum + secondnum
    elif(operator == "-"):
        result = firstnum - secondnum
    elif(operator == "*"):
        result = firstnum * secondnum
    elif(operator == "/"):
        result = firstnum / secondnum
    else:
        output = False
        print("Please enter a valid operator")

    if(output):
        print("The result is: ", result)
except ValueError:
    output = False
    print("Please enter a valid number")    


