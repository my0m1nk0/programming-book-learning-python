

input_age = int(input("Enter Your Age: "));
input_gender = input("Enter Your Gender: (M / F )");
input_height = int(input("Enter Your Height: "));

if(input_age >= 18):
   if(input_gender == "M"):
    if(input_height >= 170):
        print("You are legal to Register");
        if(input_age >= 21):
            print("You are eligible to marry");
    else:
        print("You are not Legal to register , because your height is less than 170");#break
   elif(input_gender == "F"):
    if(input_height >= 165):
        print("You are legal to Register");
    else:
        print("You are not Legal to register , because your height is less than 165");
   else:
    print("You are not Legel, Male or Female");
else:
    print("You are not legel to register , because your age is less than 18");


if(input_age >= 18):
    if(input_gender == "M") and (input_height >= 170):
        print("You are legal to Register");
    else:
        print("You are not Legal to register , because your height is less than 170");
elif(input_age < 18):
    print("You are not legel to register , because your age is less than 18");


#year = int(input("Enter a brith year: "));
#month = int(input("Enter a brith month: "));
#day = int(input("Enter a brith day: "));

#current your age (20 yr 10 month 10 day)


# age 23, M, passport, 80 kg , 170 cm,Owic, smart, 

#w ,s ,E , =>  b.a, dip , m.a , phd  => s pass, grade 10 => w pass, Eductaion pass => 

grade = int(input("Enter Your Grade: "));
language = input("Enter Your Language: (m , e ,math , s,p, c))");
if(grade < 40):
    if(grade >=35 ):
        print("Exam passed");
    else:
        print("Exam Failed");
elif(grade == 80):
    if(grade >= 75 and language == "m"):
        print("Exam passed With Distinction");
    else:
        print("Exam passed With Distinction");
else:
    if(grade == 30):
        print("You need to improve your grade");
    print("Exam Passed");

