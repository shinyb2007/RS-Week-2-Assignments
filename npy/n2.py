import numpy as np

a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print("First Row:")
print(a[0,:])

print("\nSecond Column:")
print(a[:,1])

print("\nElement 50:")
print(a[1,1])