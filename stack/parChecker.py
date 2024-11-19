from impl_stack import Stack

def par_checker(symbolString):
# str = arr => character of square brackets
# "hello world" => character of double quotes=> [h,e,l,l,o, ,w,o,r,l,d]
    st = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            st.push(symbol)
        else:
            if st.is_empty():
                balanced = False
            else:
                st.pop()
        index = index + 1
    if balanced and st.is_empty():
        return True
    else:
        return False


# ["(","(" ,"("]
res = par_checker("((())))")

print("Checking is => ",res)