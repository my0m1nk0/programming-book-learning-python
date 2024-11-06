# def printHello():
#     print("HELLO")
    
# printHello()

# def => keyword to define a function
# function_name => name of the function (printHello , startCar)
# () => parameters
# CamalCase = "CamalCase" => printHello
# userLogin()
# userLogout()
# userRegister()
# userDelete()

# hello_function.py 
# helloFunction.py

def printHello():
    print("HELLO");


def powerOff():
    print("POWER OFF");

def restart():
    print("RESTART");

def sleep():
    print("SLEEP");

input = input("Enter the function name: (off, restart, sleep): ")

if input == "off":
    powerOff()
elif input == "restart":
    restart()
elif input == "sleep":
    sleep()        
else:
    printHello()    

def printHello():
    return "HELLO";


hello = printHello();

print(hello);
