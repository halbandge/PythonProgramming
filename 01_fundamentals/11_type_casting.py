'''
type casting:

int()
float()
bool()
str()
'''

# 1. int(): we can use this function to convert from other types to int
# we can convert any type to int type except complex type
# if we want to convert str to int type, string should represent only integral value
# and should be specified only in decimal form (base-10)

print(int(10.5)) # 10
print(int(10.9)) # 10
print(int(True)) # 1
print(int('100')) # 100
# print(int('10.5')) -> error

# 2. float(): we can use this function to convert from other types to float
# we can convert any type to int type except complex type
# if we want to convert str to flaot type, string should integral value or float value
# and it should be specified only in decimal form (base-10)

print(float(10)) # 10.0
print(float(True)) # 1.0
print(float('10')) # 10.0
print(float('10.5')) # 10.5

# 3. bool(): we can use this function to convert from other types to bool
# if it is 0 then False, everything else is True (for integral values, float values)
# in str, only empty string ('') it is treated as False everything else is True

print(bool(0)) # False
print(bool(1)) # True
print(bool(2)) # True
print(bool(0.0)) # False
print(bool(0.00001)) # True
print(bool('True')) # True
print(bool('False')) # True
print(bool('')) # False

# 4. str(): we can use this function to convert from other types to string
# we can convert any type to string type

print(str(10)) # '10'
print(str(10.5)) # '10.5'
print(str(True)) # 'True'
print(str(False)) # 'False'