lis = [20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1]

# F = (C*9/5 + 32)
# Schreiben Sie ein Script (ohne NumPy), welches folgende
# Angaben (Grad Celsius) in Grad Fahrenheit umrechnet!

# lis = [round(i*9/5 + 32, 2) for i in lis]
lis = [i*9/5 + 32 for i in lis]
print(lis)

# for i in lis:
#     print(f"{i:.2f}")

import numpy as np


lis = [20.1, 20.8, 21.9, 22.5, 22.7, 21.8, 21.3, 20.9, 20.1]
arr = np.array(lis)

arr = arr*9/5 + 32
print(arr)
np.set_printoptions(precision=2, floatmode='fixed')
print(arr)
