import numpy as np

l=[1,2,3,4,5,6]
l2=[]

for element in l:
    l2.append(element+3)
print(l2)


arr=np.array([1,2,3,4,5,110])
print(arr)
arr=arr+3
print(arr)
print(type(arr))


print(arr.mean())
print(arr.min())
print(arr.max())
