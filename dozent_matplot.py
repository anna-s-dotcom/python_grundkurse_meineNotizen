import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 50, 0.5)

y = 3*x + 4

plt.plot(x, y)
plt.xlabel('X - Achse')
plt.ylabel('Y -Achse')
plt.title('y = 3*x + 4')
plt.show()
