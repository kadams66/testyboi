import numpy as np
import os
import sys

a = 3
b = 20
c = 1E7
arr = np.zeros(a)
for i in range(a): arr[i] = (i + 1) * b
arr2 = np.zeros([a, a])
for i in range(a):
    for j in range(a):
        arr2[i, j] = (i + 1) * j

print(arr2)
print(arr2 @ arr)
print(format(int(c), ','))

print('extra stuff')
print(os.getcwd())
print(sys.argv)
print(arr @ arr2 @ arr)
