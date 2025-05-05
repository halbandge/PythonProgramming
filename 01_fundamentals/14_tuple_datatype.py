# Tuple

# it is exactly same as list except that it is immutable
# read only version of list -> tuple
# it is represented using paranthesis () 
# insertion order is preserved
# indexing and slicing concepts are applicable
# duplicates are allowed
# heterogeneous objects are allowed
# it is not growable

t = (10, 20, 30, 40, 10, 'python')
print(t) # (10, 20, 30, 40, 10, 'python')
print(type(t)) # <class 'tuple'>

print(t[0]) # 10
print(t[-1]) # python

print(t[2:4]) # (30, 40)

# t[0] = 7777 -> this will throw an error since we cannot change the content of tuple