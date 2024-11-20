from stack_class.impl_stack import Stack

def number_to_binary(number):

    stack = Stack()
    while number > 0 :
        result = number % 16
        #[2,9,12]
        stack.push(result)
        number = number // 16

    binary_number = ''
    while not stack.is_empty():
        result = stack.pop()
        if result == 10:
            binary_number += "A"
        elif result == 11:
            binary_number += "B"
        elif result == 12:
            binary_number += "C"
        elif result == 13:
            binary_number += "D"
        elif result == 14:
            binary_number += "E"
        elif result == 15:
            binary_number += "F"
        else:
            binary_number += str(result)

         # binary_number += str(stack.pop())

    return  binary_number


res = number_to_binary(668)

print("Binary",res)



