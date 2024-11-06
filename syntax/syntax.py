
maxnumber = 10; #assign 10 to maxnumber
def findMax():
    maxnumber = 40; #assign 20 to maxnumber
    print('Inside function',maxnumber); #20
if 'a' == 'b' :
    maxnumber = 20;
    print('Inside if block');
    print('is equal',maxnumber);
else:
    # maxnumber = 30; #reassign 30 to maxnumber
    print('Inside else block');
print('is not equal',maxnumber); 
   
findMax();
print('outside if block',maxnumber);#30