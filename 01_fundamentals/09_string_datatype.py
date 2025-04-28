# any sequence of characters within 
# either single quotes 
# or double quotes 
# or triple quotes is called as strings

# s0 = python -> invalid string
s = 'python' # valid string
s1 = "python" # valid string
s2 = """python""" # valid string

print(type(s)) # <class 'str'>
print(type(s1)) # <class 'str'>
print(type(s2)) # <class 'str'>

s3 = """
        python
        programming   
        language
     """ # this is called as multiline string literal and it can be only done with triple quotes
print(s3, type(s3))

# expected output: Python classes by 'John Doe' are average

# s = 'Python classes by 'John Doe' are average' -> invalid string (this will throw an error)
s4 = "Python classes by 'John Doe' are average" # if the outer string is double quotes we can use single quotes inside a string
s5 = 'Python classes by "John Doe" are average' # if the outer string is single quotes we can use double quotes inside a string
s6 = """Python 'classes' by "John Doe" are average""" # if the outer string is triple quotes we can use both single and double quotes inside a string

print(s4) # Python classes by 'John Doe' are average
print(s5) # Python classes by "John Doe" are average
print(s6) # Python 'classes' by "John Doe" are average

# we can also write s6 string with single and double quotes as well but for that we have to use escape character
# escape character will tell that we want to symbol quotes (inside of considering as a string)
# in python to do that escape character is \ 
# for e.g.

s7 = 'Python \'classes\' by "John Doe" are average'
s8 = "Python 'classes' by \"John Doe\" are average"

print(s7) # Python 'classes' by "John Doe" are average
print(s8) # Python 'classes' by "John Doe" are average

# NOTE: We can also say that s6, s7 and s8 are different ways of representing the same string in different ways



