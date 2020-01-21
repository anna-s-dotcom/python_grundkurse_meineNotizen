import matplotlib.pyplot as plt

labels = ['dreizig', 'vierzig', 'zehn', 'zwanzig']
data = [30, 40, 10, 20]
colors = ['b', 'y', 'r', 'g']
explode = [0, 0, 0, 0.1]

plt.pie(data, labels = labels, explode = explode, colors = colors)
plt.show()
