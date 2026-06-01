import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6]
])

print("Array:")
print(a)

print("\nShape:")
print(a.shape)

print("\nSize:")
print(a.size)

print("\nDimensions:")
print(a.ndim)

print("\nDatatype:")
print(a.dtype)

a = a.astype(float)

print("\nAfter Datatype Conversion:")
print(a)

print("New Datatype:")
print(a.dtype)