import numpy as np

# mat = np.asarray([[1, 2], [3, 40]])
mat = np.array([[1, 0], [3, 40]])
print(mat)

bool_mat = np.array([[1, 0], [3, -40]], bool)
print(bool_mat)

float_mat = np.array([[1, 0], [3, -40]], float)
print(float_mat)

int_mat = np.array([[1.5, 0], ['3', -40]], int)
print(int_mat)
