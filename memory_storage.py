import platform
import sys

p =  platform.architecture()
is_64bits = sys.maxsize > 2**32
#128 bit 
a = 340282366920938463463374607431768211456999999999
print(type(a))
print(a)
