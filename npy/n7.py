





# Python List is a built-in data structure of Python.
# NumPy Array is provided by NumPy library.

# Lists are slower for numerical calculations while
# NumPy arrays are faster and use less memory.

# In lists, '+' joins two lists together.
# In NumPy arrays, '+' performs element-wise addition.


#example -

import numpy as np

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("List Addition:")
print(list1 + list2)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nNumPy Array Addition:")
print(a + b)