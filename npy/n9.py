



# dtype is used to check the datatype of a NumPy array.

# astype() is used to change the datatype of a NumPy array.

# Example:
# a.dtype  checks datatype
# a.astype(float)  converts datatype to float

#example -

import numpy as np

a = np.array([1, 2, 3, 4])

print("Original Array:")
print(a)

print("\nDatatype:")
print(a.dtype)

b = a.astype(float)

print("\nArray after Conversion:")
print(b)

print("\nNew Datatype:")
print(b.dtype)