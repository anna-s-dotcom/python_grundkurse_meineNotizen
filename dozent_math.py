import numpy as np

print('np.ceil(0.1):', np.ceil(0.1))
print('np.floor(0.9):', np.floor(0.9))

# rundet immer zur nächsten geraden Zahl hin (bei .5)
print('np.round(2.5)', np.round(2.5))
print('round(2.5)', round(2.5))
print('np.round(3.5)', np.round(3.5))
print('round(3.5)', round(3.5))

# erstellt array mit fünf einträgen zwischen 0 und 100 (gleichverteilt)
print(np.random.uniform(0, 100, 5))

# erstellt array mit shape (3, 4) - einträge sind zufällige zahlen zwischen 0 und 10
print(np.random.rand(3, 4)*10)
print()

# erstellt matrix mit allen einträgen == 0
print(np.zeros((2, 5)))

# erstellt matrix mit allen einträgen == 1
print()
print(np.ones((2, 5)))

# erstellt identitätsmatrix
print()
print(np.identity(3))

# überall 0, außer zeile = spalte -> 1
print()
print(np.eye(4, 5))

# matritzen multiplikation

m1 = np.array([1, 2, 2, 1, 1, 1]).reshape(3, 2)
m2 = np.array([2, 1, 1, 2]).reshape(2, 2)

print()
print('Matritzenmultiplikation')
print(m1)
print()
print(m2)
print()
print(m1.dot(m2))
print()
print(np.dot(m1, m2))
print()
print(m1@m2)
