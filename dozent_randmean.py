import random
import time

t = time.time()
lis = [random.randint(1,10) for i in range(100000)]
print('List:', time.time()-t)
# # mit for schleife:#
t = time.time()
lis = []
for i in range(100000):
    lis.append(random.randint(1,10))
print('For:', time.time()-t)
# print(lis)
t = time.time()
m = sum(lis)/len(lis)
print('List Mean:', time.time()-t)
# print(m)

import numpy as np
t = time.time()
arr = np.random.randint(1, 11, size = 100000)
print('Numpy:', time.time()-t)
# print(arr)
t = time.time()
m = arr.mean()
print('NumPy Mean:', time.time()-t)
# print(m)
