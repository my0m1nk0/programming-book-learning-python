count = int(input("Enter the number of terms: "))

a, b = 1, 1 #
if(count <= 0):
    print("Please enter a positive integer")
else:    
    print("Fibonacci sequence:")
    for _ in range(count):
        print(a, end=' ') # 0 1 1 2 3
        a, b = b, a + b 
        #first time ( a = 1 , b = 1) 
        # 1
        #second time ( a = 1 , b = 2)
        # 1 1
        #third time ( a = 2 , b = 3)
        # 1 1 2
        #fourth time ( a = 3 , b = 5)
        # 1 1 2 3
        #fifth time ( a = 5 , b = 8)
        # 1 1 2 3 5
        #sixth time ( a = 8 , b = 13)
        # 1 1 2 3 5 8
        #seventh time (a = 13 , b = 21)
        # 1 1 2 3 5 8 13
        # Fibonacci sequence: 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765

