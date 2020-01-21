import numpy as np

arr = np.array([[1, 5, 8, 4],[0, 3, 6, 9], [4, 7, 9, 5]])
print(arr)

print(arr.shape)
onedim = arr.ravel()
print(onedim)
print(onedim.shape)
new_mat = onedim.reshape(3,4)
print(new_mat)
print(new_mat.shape)
