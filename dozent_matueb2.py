import numpy as np

m = np.random.randint(1, 11, (3, 4))

print(m)
print()

first = m[0][0]
print(first)

first = m[0, 0]
print(first)

firstline = m[0]
print(firstline)

firstline = m[0, :]
print(firstline)

firstcol = m[:, 0]
print(firstcol)

firstcol = firstcol.reshape(-1, 1)
print(firstcol)

firstcol = firstcol.ravel()
print()
print(firstcol.shape)
firstcol = firstcol[:, np.newaxis] # firstcol[:, None]
print(firstcol.shape)
