import numpy as np

a = np.arange(1,13)

print("Original Array:")
print(a)

print("\nShape (3,4)")
print(a.reshape(3,4))

print("\nShape (2,6)")
print(a.reshape(2,6))

print("\nShape (2,3,2)")
print(a.reshape(2,3,2))