# List

# if we want to represent a group of values as a single entity, where insertion order preserved
# and duplicates are allowed.
# List is represented using [] i.e. square brackets
# 1. insertion order preserved
# 2. duplicate objects are allowed
# 3. heterogeneous objects are allowed
# 4. values should be enclosed within []
# 5. index and slice are applicable
# 6. it is growable in nature (i.e. it is mutable)

l = [10, 10.5, 'python', True, 10]
print(l)
print(type(l)) # <class 'list'>

# we can do indexing and slicing same way as we were able to do for string

print(l[0]) # 10
print(l[-1]) # 10
print(l[2:5]) # ['python', True, 10]