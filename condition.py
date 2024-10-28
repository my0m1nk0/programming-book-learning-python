
firstNum = input("Enter first number: ");
secondNum = input("Enter second number: ");

try:
    firstnum = int(firstNum);
    secondnum = int(secondNum);
    if(secondnum  <= 0):
        print("Please enter second number greater than 0");    
    else:
        divide = firstnum / secondnum;
        print("Divide of two numbers",firstNum,"and",secondNum,"is ",divide);
except ValueError:
    print("Please enter integer number");
