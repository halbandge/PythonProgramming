a = 12345666666666666677777777777777778888888888888889999999
print(a)
print(type(a)) # <class 'int'>

# we can represent integral values in four ways

# 1. decimal form (base-10) => 0,1,2,3,4,5,6,7,8,9
# 2. binary form (base-2) => 0,1
# 3. octal form (base-8) => 0,1,2,3,4,5,6,7
# 4. hexadecimal form (base-16) => 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F or 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f

a = 1111
print(a) # this is decimal form since default base is base 10

# to represent in binary form we use 0b or 0B
bin_num = 0b1111
print(bin_num) # 15 => 1 * 2^0 + 1 * 2^1 + 1 * 2^2 + 1 * 2^3
print(type(bin_num)) # <class 'int'>

# to represent in octal form we use 0o or 0O
octal_num = 0o123
print(octal_num) # 83 => 3 * 8^0 + 2 * 8^1 + 1 * 8^2 

# to represent in hexademial form we use 0x or 0X
hex_num = 0xFACE
print(hex_num) # 64206 => 15 * 16^3 + 10 * 16^2 + 12 * 16^1 + 14 * 16^0