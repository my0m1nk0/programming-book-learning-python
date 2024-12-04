def binary_search(array,item):
    first = 0
    last = len(array) - 1
    while first <= last:
        mid = (first + last)//2
        mid_value = array[mid]
        if mid_value == item:
            return True
        else:
            if item < mid_value :
                last = mid - 1
            else:
                first = mid + 1
                return False

print(binary_search([8,14,18,20,26,66,78],18))
print(binary_search([8,14,18,20,26,66,78],19))
