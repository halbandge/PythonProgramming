# complex format in python is a + bj
# where a is real number and b is imaginary number
# and j^2 = -1 so j = squareroot(-1)

c = 10 + 20j
c1 = 10 + 20J

print(c, c1) # we can use either j or J -> (10+20j) (10+20j)

# for a, b we can use both int and float values

c2 = 10.5 + 20.6j

print(type(c)) # <class 'complex'>
print(type(c1)) # <class 'complex'>
print(type(c2)) # <class 'complex'>

# to get real and imaginary part from the complex number
# we can use .real and .imag 

# example
c3 = 1.32 + 432.243j
print(c3.real) # 1.32 -> gives the real part of complex number
print(c3.imag) # 432.234 -> gives the imaginary part of complex number