    # range =>[1, 2, 3, 4, 5, 6, 7, 8, 9,10 ];
    # index => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for product in range(10):
    print(product)
print('-------------------');
products = ['iphone', 'samsung', 'nokia', 'huawei', 'sony', 'lg', 'htc', 'blackberry', 'motorola', 'oneplus'];
for i in products:
    print(i);
print('-------------------');
for i in products[:5]:
    print(i);
print('-------------------');
for i in range(5, 10):
    print(i);

if(products):
    for i in products:
        if(i == 'nokia'):
            print('Found Nokia');
            break;
else:
    print('No products found');

for i in products:
    if(i == 'nokiaaa'):
        print('Found Nokia');
        break;
    else:
        print('No products found');        

# for variable in data => data can be a list, tuple, set, string, dictionary

