#eine schleife in der anderen
#verschachtete Schleifen

for i in range(3):
    print("Außen", i)
    for j in range(3):
        print("Innen",j)


#Ausgabe:
# Zeile 0: 0 1 2
#Zeile 1: 0 1 2
#
#Zeile n: 0 1 2
#äußere schleife ==ganze Zeilen
#end="" - kein Bruch, in einer Zeile

for i in range(10):
    print(f"Zeile {i}: ", end=" ")
    for j in range(3):
        print(j, end= " ")
