# print(15 in [3,5,2,4,1])
# print(4 in [3,5,2,4,1])
k = [1,2,51,34,37,78]
s = 3

for i in k:
    if i == s :
        print("found")
        break



def search(array,search_value):
    for (index,value) in enumerate(array):
        if value == search_value :
            return index
    return -1

res = search([1,2,51,34,37,78],371)
if res != -1 :
    print("Found at ",res)
else:
    print("Not found")