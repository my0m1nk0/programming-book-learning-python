num = int(input("Enter the number of terms: "))

for i in range( num ): 
    i = i + 1
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")