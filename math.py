import numpy as np

print("ceil(0.1):", np.ceil(0.1)) #zaokraglenie do calej liczby
print("floor(0.9):", np.floor(0.9)) #zaokraglenie w dol


print("round(2.5):", np.round(4.6)) # zaograglenie do calej liczby po przecinku (gerade Zahl)
print("round(2.5):", round(2.6)) # zaograglenie do calej liczby

#100 ist nicht dabei, zufällige zahl ausgeben, jede zahl hat eine chance, geworfen zu werden
print(np.random.uniform(0,100,9))

#zufällige zahl zwischen 0 und 1 in diesem Format 3 Spalten, 3 Zeilen, *10-zwischen 0 und 10
print(np.random.rand(3,3)*10)

#erstellt matrix mit allen  einträgen==0

print(np.zeros((2,5)))

#erstellt matrix mit allen  einträgen==1

print()
print(np.ones((2,5)))

#erstellt identitätsmatrix
print()
print(np.identity(3))

#erstellt identitätsmatrix, aber mehr flexibler gestallbar
print()
print(np.eye(4,5))

#matrizen multiplikationen

m1=np.array([1,2,2,1,1,1]).reshape(3,2)
m2=np.array([2,1,1,2]).reshape(2,2)

print("Matrizen multiplikation")
print(m1)
print()
print(m2)

#matrizen multiplizieren m1 und m2
print("Ergebnis")
print(m1.dot(m2))
print(m1@m2)
