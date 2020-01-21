import numpy as np

arr1 = np.arange(10)
print(arr1)

arr2 = np.arange(5, 10)
print(arr2)

arr3 = np.arange(5, 10, 2)
print(arr3)

arr4 = np.linspace(4, 6, 10)
print(arr4)

print()
print('arr1[(arr1 > 6) | (arr1 < 4)]')
print(arr1[(arr1 > 6) | (arr1 < 4)])
print()
print('arr1 > 6 | arr1 < 4')
print((arr1 > 6) | (arr1 < 4))

print(arr1)

print()

randarr = np.random.randint(0, 11, 10)
print(randarr)
# randarr wird nicht verändert
sortarr = np.sort(randarr)
print(sortarr)
print(randarr)
# # randarr wird verändert
# randarr.sort()
# print(randarr)
args = np.argsort(randarr)
print(args)
