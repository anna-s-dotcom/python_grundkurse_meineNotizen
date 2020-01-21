import numpy as np
import time
np.set_printoptions(precision=2, floatmode="fixed")

lis=[20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1]
lis2=[]

for element in lis:
    lis2.append(round((element*9)/5+32,2))
print(lis2)


arr=np.array([20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1])
print(arr)
arr=arr*9/5+32
print(arr)
print(arr[0])

x=0
l1=[1,5,8,4,7,3,2,2,6,8]



mw=sum(l1)/len(l1)

print(mw)

arr=np.array([1,5,8,4,7,3,2,2,6,8]).mean()
print(arr)

#
t=time.time()
arr=np.random.randint(1,11,size=1000000000)
print("Zeit", time.time()-t)
