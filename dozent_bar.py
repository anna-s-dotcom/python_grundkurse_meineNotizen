import numpy as np
import matplotlib.pyplot as plt

x_pos = np.arange(4)

data = [40, 30, 20, 10]
labels = ['vierzig', 'dreißig', 'zwanzig', 'zehn']
colors = ['b', 'y', 'r', 'g']

plt.bar(x_pos, data,
        color = colors,
        edgecolor = 'k',
        zorder = 10,
        alpha = 0.8)
plt.xticks(x_pos, labels)
plt.grid(which = 'major',
        linestyle = ':',
        linewidth = 1.5,
        color = 'k',
        zorder = 0)
plt.minorticks_on()
plt.grid(which = 'minor',
        linestyle = '-.',
        linewidth = 0.5,
        color = 'gray',
        zorder = 0)
plt.show()
