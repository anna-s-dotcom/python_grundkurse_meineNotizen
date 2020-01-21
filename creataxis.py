import numpy as np

arr1=np.arange(10)
print(arr1)
arr2=np.arange(5,10)
print(arr2)

arr3=np.arange(5,10,2)
print(arr3)

#achse von 4 bis 6, 10 Punkte wurden aufgetragen
arr4=np.linspace(4,6,10)
print(arr4)

print("arr1[arr1>4]") # gibt nur True Elemente, neue Liste
print(arr1[(arr1>6)| (arr1<4)])
print((arr1>6)|(arr1<4)) # oder


randarr=np.random.randint(0,11,10)
print(randarr)
sortarr=np.sort(randarr)
print(sortarr)
print(randarr)
args=np.argsort(randarr)
print(args)
