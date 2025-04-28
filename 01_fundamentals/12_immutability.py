# Fundamental Data Types vs Immutability in Python
# --------------------------------------------------

# In Python, everything is treated as an object.
# Some objects are 'immutable', meaning their content cannot be changed after creation.
# If we attempt to modify an immutable object, Python creates a new object instead.

# Example with integers (which are immutable):

x = 10  # Assign an integer value to x
print("ID of x (initial):", id(x))  # Print the memory address (ID) of x

x = x + 1  # Modify x (actually creates a new object and reassigns x)
print("ID of x (after x + 1):", id(x))  # ID changes, indicating a new object was created

# Since the ID of 'x' before and after modification is different,
# it confirms that a new object has been created.

# If an object has no references pointing to it, Python's garbage collector will automatically clean it up.

# Demonstrating multiple references:

x1 = 10  # Create an integer object and assign to x1
y1 = x1  # Make y1 reference the same object as x1

print("ID of x1:", id(x1))  # ID of x1
print("ID of y1 (same as x1):", id(y1))  # ID of y1, should be same as x1

# Both x1 and y1 are referencing the same object currently.

y1 = y1 + 1  # Modify y1 (creates a new object)

print("ID of x1 (after y1 changes):", id(x1))  # ID of x1 remains the same
print("ID of y1 (new object):", id(y1))  # ID of y1 changes, indicating a new object

# After modifying y1, it now points to a new object.
# x1 still points to the original object, hence no garbage collection is needed here.

# Summary:
# --------
# - Immutable objects (like integers) cannot be changed. Any 'modification' results in a new object.
# - Variables can share references to the same object.
# - Modifying one variable that points to an immutable object will not affect others.
# - Python automatically manages unused objects using garbage collection.
