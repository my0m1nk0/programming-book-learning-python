def binary_search(array, item):
    if len(array) == 0:
        return False

    mid = len(array) // 2
    mid_value = array[mid]
    if mid_value == item:
        return True
    else:
        if item < mid_value:
            return binary_search(array[:mid], item)
        else:
            return binary_search(array[mid + 1:], item)


print(binary_search([8, 14, 18, 20, 26, 66, 78], 18))
print(binary_search([8, 14, 18, 20, 26, 66, 78], 19))