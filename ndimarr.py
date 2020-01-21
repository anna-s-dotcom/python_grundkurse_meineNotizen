import numpy as np


# mat=np.array([[1,2],[3,4]])
# print(mat)
#
# bool_mat=np.array([[0,2],[3,4]],bool)
# print(bool_mat)
#
# float_mat=np.array([[0,2],[3,4]],float)
# print(float_mat)
#
# int_mat=np.array([['0',2],[3,'4']], int)
# print(int_mat)

arr=np.array([[1,5,8,4],[0,3,6,9],[4,7,9,2]])
print(arr)
#zahl der elemente
onedim=arr.ravel()
print(onedim)
print(onedim.shape)

#als tulpe ausgeben, 3 zeilen, 4 spalten
new_mat=onedim.reshape(3,4)
print(new_mat)
print(new_mat.shape)
