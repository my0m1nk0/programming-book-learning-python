# list = [1048,1255,2125,1050,2506,1236,2010,1055]

# maxnumber = list[0]

# for x in list:
#     if maxnumber < x :
#         maxnumber = x

# print("MAX number in array is”,maxnumber)
lis = [1048,1255,2125,1050,2506,1236,2010,1055];
"""
this function will return max number from list
we can pass list as argument or we can use default list
default list is lis

"""
def findMax(list = lis):
    maxnumber = list[0];
    for i in list:
        if maxnumber < i :
            maxnumber = i

    return maxnumber;        

max_number = findMax();

numList =[1,2,5,6,9,3,2];

max_number = findMax(numList);

print("MAX number in array is",max_number);