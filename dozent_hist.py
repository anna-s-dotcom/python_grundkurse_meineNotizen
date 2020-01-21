import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 91, 100)

n, bins, patches = plt.hist(x, [0, 30, 60, 90],
                            edgecolor = 'k',
                            color = 'r')
plt.show()

print(n)
print(bins)
print(patches)
