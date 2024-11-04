list = [1,5,2,7,8,9,200,155]
result = 0
data = 0
for a in list:
    result = result + a
print(result)
print("_________________________")    
for i in range(len(list)) :
    data = data + list[i]
    if(list[i] == 200):
        print("200 found")
        break
print(data)   