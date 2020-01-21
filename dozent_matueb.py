import numpy as np
# Erstelle zwei 4*4 Matrizen mit zufälligen Zahlen.
# 1) Erstelle eine Matrix, welche in jedem Element das Produkt der anderen Matrizen hat.

# A = np.array([[1 , 2],[2, 3]])
# B = np.array([[2 , 4],[1, 3]])
# C = [[1*2, 2*4], [2*1, 3*3]]
# C = A*B

m1 = np.random.randint(1, 11, (4,4))
m2 = np.random.randint(1, 11, (4,4))

m3 = m1 * m2
print(m1)
print()
print(m2)
print()
print(m3)
# 2) Erstelle eine Matrix, welche durch die Matritzenmultiplikation der ersten beiden entsteht.
# m4 = m1.dot(m2)
# m4 = np.dot(m1, m2)
m4 = m1@m2
print()
print(m4)
