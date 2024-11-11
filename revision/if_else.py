#or nor and
#if else elif

# user_input = input("Do you want to exit:(y/n) ")
# if user_input == "y":
#     print("Exiting the program")
# else:
#     print("Continuing the program")

#calculator
# + - * / %
# 3 / 5
#sum function>>> u need to fill 2 parameters or arguments
#Boolen , String , Int , List
#Error Handling
def sum_number(first , second):
   try:
     sums =  int(first) + int(second)
     return sums
   except ValueError:
       print("Enter Number Only")

#Sub Function
def sub_number(number1 , number2):
    try:
        sub = int(number1) - int(number2)
        return sub
    except ValueError:
        print("Enter Number Only")

userInput = input("Enter Operator : ")
firstNum = input("Enter First Number : ")
secondNum = input("Enter Second Number : ")
if userInput == "+" :
   total = sum_number(firstNum,secondNum)
   print(total)
elif userInput == "-" :
    if firstNum < secondNum:
        print("Invalid Operation")
    else:
        total = sub_number(firstNum,secondNum)
        print(total)
elif userInput == "*" :
    def multi_num():
        return int(firstNum) * int(secondNum)
    print(multi_num())
elif userInput == "/" :
    if firstNum < secondNum:
        print("Invalid Operation")
    else:
        print('Div')
else:
    print('Invalid Operator')
print('Program Complete')


#function

def arr_func():
    return  ['a','b','c']


list = arr_func()

for i in list:
    print(i)






