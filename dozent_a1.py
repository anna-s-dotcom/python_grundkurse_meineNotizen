# Aufgabe:
# Teile die 10 durch alle Zahlen:
# range(-10, 10) (nutze eine for schleife)

for i in range(-10, 10):
    try:
        print(10/i)
    except Exception as e:
        print(e)
