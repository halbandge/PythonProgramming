# string indexing -> to access single element from the string
# indexing start from left start with index 0 [positive indexing]
# indexng start from right start with index -1 [negative indexing]
# we have both positive indexing and negative indexing 
# to get the index from string -> string[index_number]

# positive indexing
s = "python"
print(s[0]) # 'p'
print(s[1]) # 'y'
# print(s[10]) -> this will throw an error

# negative indexing
print(s[-1]) # 'n'
print(s[-2]) # 'o'
print(s[-6]) # 'p'

# we got only specific item/element from the string
# to get the part of a string i.e. multiple elements from string 
# for that we can use slicing
# to get the slicing from string -> string[start_index:end_index]
# it returns substring from begin index to end - 1 index

# for e.g. to 3rd index to 7th index from string
s1 = 'abcdefghijklmnopqrstuvwxyz'
print(s1[3:8]) # 'defgh'
print(s1[5:11]) # 'fghijk'

# NOTE: it is not mandatory to mention the start_index, if we dont mention it then its default value will be 0
print(s1[:8]) # from 0 to 7th index -> 'abcdefgh'

# NOTE: similarly, if we dont mention the end_index, then it will go till the end of the string
print(s1[3:]) # from 3rd index till end of string -> 'defghijklmnopqrstuvwxyz'

# if we don't mention the start_index as well end_index then we will get the entire string
print(s1[:]) # 'abcdefghijklmnopqrstuvwxyz'

# if we mention end_index greater than actual length of string, then it will still consider till end of string
# to summarise: slice operator wont raise any IndexError
# If the index is out of range, then it will consider upto available characters only
print(s1[0:5000]) # 'abcdefghijklmnopqrstuvwxyz'

# TODO: to convert string 'python' to 'Python'
s2 = 'python'
new_str = s2[0].upper() + s2[1:]
print(s2, new_str) # python Python

# Mathematical operators for the string
# 'python' + 'programming' -> 'pythonprogramming'
# 'python' * 5 -> pythonpythonpythonpythonpython
# 'python' + 10 -> error
# NOTE: if we apply + operator for the strings both the arguments should be of str type only
# 'python' + '10' -> python10 