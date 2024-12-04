
def fibonacci_sequence(n):
    if n < 2:
        return n
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

result = fibonacci_sequence(3)
print(result)