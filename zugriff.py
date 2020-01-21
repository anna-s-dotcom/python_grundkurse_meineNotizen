import numpy as np

m1=np.random.randint(1,11, (3,4))

first=m1[0,0]
print(first)

firstline=m1[0]
print(firstline)

firstline=m1[1, :]
print(firstline)


firstcolumn=m1[:,0]
print(firstcolumn)

firstcolumn=firstcolumn.reshape(-1,1)
print(firstcolumn)

firstcolumn=firstcolumn.ravel()
print()

#eindimensionale array, zu zweidimensionalen
firstcolumn=firstcolumn[:,np.newaxis]
print(firstcolumn)
