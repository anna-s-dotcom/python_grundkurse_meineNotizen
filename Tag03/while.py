#wiederholen
i=0
while i<=10:
        i+=1
        #i=i+1
        print(i)

#Aufgabe: Erstelle ein Programm, welches abfragt, ob ein bestimmter Prozess wiederholt werden sollte
#wenn "y", dann wiederhole die Abfrage, wenn "n", dann nicht
#Möchten sie sie Prozesse wiederholen y/N

antwort=input("Möchten Sie die Prozesse wiederholen")

while antwort!="nein":
    antwort=input("Möchten Sie die Prozesse wiederholen")

    if antwort !="ja" and antwort!="nein":
        print("Falsche Eingabe")
