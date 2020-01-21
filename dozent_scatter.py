import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
np.random.shuffle(x)

y = np.random.randint(0, 101, 100)

plt.scatter(x, y,
    color = np.array(['r', 'b']).repeat(50),
    edgecolor = 'k',
    alpha = 0.5,
    s = 100,
    label = 'Scatter')
plt.plot(np.sort(x), y.mean().repeat(len(x)), 'k-.')
plt.legend()
plt.show()
