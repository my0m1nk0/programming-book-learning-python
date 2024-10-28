
# b = "60"; //စာသားတန်ဖိုး //string


# a = 60;//  ဂဏန်းတန်ဖိုး //integer

# c = 60.0; // ဂဏန်းတန်ဖိုး //float

# d = True // အဆင့်တန်ဖိုး //boolean

# int() => function or method,function name 

# Varible 
#syntax, sematic, pragmetic
#Error Handling

print("******************************************")
print("******* WELCOME To SUM APP ***************");
print("******* Please Enter Number Value ********");
print("******************************************")

firstNumber = input("Enter first number: "); 
secondNumber = input("Enter second number: "); 

try: 
    intFirst = int(firstNumber); #int
    intSecond = int(secondNumber); #int
    sum = intFirst + intSecond;
    print(f"Sum of two numbers {firstNumber} and {secondNumber} is ",sum);
    print("********************************")
    print("******* THANK YOU***************");
    print("******* For Using APP **********");
    print("********************************")

except ValueError:
    print("ကျေးဇူးပြု၍ ဂဏန်းတန်ဖိုး ထည့်ပေးပါ။");    




