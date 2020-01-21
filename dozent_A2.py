# Erstelle ein array es soll die Augenanzahl enthalten, wenn mit zwei würfeln geworfen wurde. Es soll 100 mal gewürfelt werden.

# Wie häufig wurden die jeweiligen Augenanzahlen geworfen?
import numpy as np
import matplotlib.pyplot as plt

w1 = np.random.randint(1, 7, 100)
w2 = np.random.randint(1, 7, 100)

w = w1 + w2

bins = np.arange(1.5, 12.6, 1)

# print(bins)

n, bins, patches = plt.hist(w, bins, edgecolor = 'k', alpha = 0.5)
plt.plot(np.arange(2, 13), n, color = 'r')
plt.xticks(np.arange(2, 13))
plt.show()
