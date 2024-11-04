arr = ["apple", "banana", "cherry"];

for (i , item ) in enumerate(arr):
    print("Index is => ",i,"Value is => " ,item);
#ARRAY
arr = ["apple", "banana", "cherry"];

arr[0] = "kiwi";
#mutable 
print(arr);

#TUPLE
data = ("apple", "banana", "cherry");
# tuple' object does not support item assignment
data[0] = "kiwi";
 #immutable
# print(data); # ERROR

