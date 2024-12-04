def bubble_sort(array):
    for num in range(len(array) - 1,0,-1):
        for i in range(num):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array

alist = [1,6,4,7,8,9]
print(bubble_sort(alist))