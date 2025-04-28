'''
type casting:

int()
float()
complex()
bool()
str()
'''

# 1. int(): we can use this function to convert from other types to int
# we can convert any type to int type except complex type
# if we want to convert str to int type, string should represent only integral value
# and should be specified only in decimal form (base-10)

print(int(10.5)) # 10
print(int(10.9)) # 10
# print(int(10 + 20j)) -> error
print(int(True)) # 1
print(int('100')) # 100
# print(int('10.5')) -> error