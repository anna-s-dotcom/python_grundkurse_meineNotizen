import numpy as np

arr = np.arange(0, 6*np.pi, 0.01)
# print(arr)
np.random.shuffle(arr)
# print(arr)
x = arr.copy()
y = np.sin(x)
print(x)
print(y)
i = np.argsort(x)
print(i)
print(x[i])
print(y[i])
import matplotlib.pyplot as plt
plt.plot(x[i], y[i])
plt.show()
