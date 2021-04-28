import numpy as np
import os
import sys

a = 3
b = 20
c = 1E7
arr = np.zeros(a)
arr += b
arr2 = np.zeros([a, a])
for i in range(a):
    for j in range(a):
        arrs[i, j] = (i + 1) * j

print(a / b)
print(arrs @ b)
print(format(c, '%d'))

print(sys.argv)
