num = 10
count =1
a , b = 0, 1 #destructuring assignment

while count <= num:
    a, b = b, a + b
    print(a, end=' ')
    count += 1




