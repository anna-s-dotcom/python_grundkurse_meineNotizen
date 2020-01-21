# Plotte den Cosinus von X (von -2*PI bis 2*PI)
# Beschrifte den Graph
import numpy as np
import matplotlib.pyplot as plt


# x = np.arange(-2*np.pi, 2*np.pi, 0.01)
x = np.linspace(-2*np.pi, 2*np.pi, 100)

ycos = np.cos(x)
ysin = np.sin(x)

plt.plot(x, ycos, label = 'Cosinus', color = 'k', linestyle = '--', linewidth = 5.5)
plt.plot(x, ysin, label = 'Sinus', color = '#FF0000', linestyle = '-')
plt.title('Cosinus + Sinus')
plt.xlabel('x - Achse')
plt.ylabel('y - Achse')
plt.legend(loc = 1) # 'upper right'
plt.margins(0.1)
plt.xlim(-np.pi, np.pi)
plt.ylim(-2, 2)
plt.show()
