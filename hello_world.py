print("hello World")
x=5
y=6
z=x+y

print(f"""6+5 {6+5}""")
print()

print("6-5\n" +str(6-5))
print()


#alles was in format() steht wird als string  berechnet anstelle von {} ausgegeben
print(z+y)

print("11 % 2")
print(11 % 2)
print("11//2")
print(11//2)

print("5+6")
print(5+6)

print("3*4")
print(3*4)
print("11//2:", 11//2, sep="...")

# f"..." alle Werte in {} werden berechnet und ausgegeben
print(f"6/5:{6/5}")
print()

#zwei strings werden zusammengefügt

print("11%2: " + str(11%2))
print()

#ausgabe vo zwei wertenm string und berechnung
print("11/2:", 11//2)
print()

#boolsche ausdrücke gleich: ==, da= ein zuweisungsoperator ist
print('Boolean:')
print(11<10)
print(11<12)
print(11>=11)
print(23==23.5)
#!=ungleich
print(23 !=23)
print(True==True)
#none None ist der leere Wert
x=None
print(x)
#str(x) gibt einen string zurück mit wert"x"
x=7
x=str(x)
print(type(x))

x=int("45")
print(type(x))
