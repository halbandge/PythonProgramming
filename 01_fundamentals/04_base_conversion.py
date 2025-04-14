# bin() -> converts other base forms to binary form (base 2)
print(bin(15)) # 0b1111
print(bin(0o123)) # 0b1010011
print(bin(0xFACE)) # 0b1111101011001110

# oct() -> converts other base forms to octal form (base 8)
print(oct(100)) # 0o144
print(oct(0b11101)) # 0o35
print(oct(0xFACE)) # 0o175316

# hex() -> converts other base forms to hexadecimal form (base 16)
print(hex(1000)) # 0x3e8
print(hex(0b10111111)) # 0xbf
print(hex(0o123456)) # 0xa72e