import numpy as np

a = np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
])

print("Original Array:")
print(a)

print("\nFirst Column:")
print(a[:,0])

print("\nLast Row:")
print(a[2,:])

print("\nRequired Subarray:")
print(a[0:2,1:3])