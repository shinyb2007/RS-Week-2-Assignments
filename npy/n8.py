import numpy as np

a = np.array([1,2,3,4])

print("Before Conversion:")
print(a)
print(a.dtype)

a = a.astype(float)

print("\nAfter Conversion:")
print(a)
print(a.dtype)