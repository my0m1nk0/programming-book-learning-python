from stack_class.impl_stack import Stack

def parCheck(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
            else:
                s.pop()
        index += 1
    if balance and s.is_empty():
        return True
    else:
        return False


res = parCheck('{[()]}')
print(res)
