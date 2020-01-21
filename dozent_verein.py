# Erstelle eine Klasse: Verien
# Attribute: name,  vorsitz,  vorstand (Liste),  mitglieder (Liste)
# Methoden vorstandWaehlen(),  vorsitzendenWaehlen(),  mitgliedHinzufuegen(),  mitgliedEntlassen()
# 1) Die Klasse Verein bekommt bei der Initialisierung nur den Namen zugewiesen.

import random

class Verein:
    def __init__(self, name):
        self.name = name
        self.vorsitz = None
        self.vorstand = []
        self.mitglieder = []

# 2) Erstelle eine Methode,  die dem Verein Mitglieder hinzufügt.

    def mitgliedHinzufuegen(self, m):
        self.mitglieder.append(m)

    # # wenn self.mitglieder nicht in der __init__()
    # def mitgliedHinzufuegen(self, m):
    #     try:
    #         self.mitglieder.append(m)
    #         print('erfolgreich')
    #     except:
    #         print('existiert noch nicht')
    #         self.mitglieder = []
    #         self.mitglieder.append(m)

# 3) Erstelle eine Methode,  die genau fünf Mitglieder dem Vorstand zuweist.
# (Manuelle Zuweisung (über die Liste gehen) oder zufällig mit:
# import random → random.choice() : wählt ein zufälliges Element einer Liste)

    def vorstandWaehlen(self):
        n = 5
        if len(self.mitglieder) >= n:
            self.vorstand = random.sample(self.mitglieder, n)

# 4) Erstelle eine Methode,  die ein Vorstandsmitglied zum Vorsitzenden macht.
    def vorsitzendenWaehlen(self):
        if len(self.vorstand) > 0:
            self.vorsitz = random.choice(self.vorstand)
# 5) Erstelle eine Methode,  die ein bestimmtes Mitglied aus dem Verein löscht.
    def delMitglied(self):
        repeat = True
        while repeat:
            name = input('Bitte gültigen Namen eingeben: ')
            for i in range(len(self.mitglieder)):
                if name == self.mitglieder[i]:
                    self.mitglieder.pop(i)
                    repeat = False
                    break

# 6) Erstelle eine oder mehrere Methoden um Mitglieder,  Vorstand,  Vorsitz,  den ganzen Verein
# auszugeben

names = ["Tasha Ostrow", "Rufina Rosell", "Ray York", "Ada Mcgonigal", "Mertie Broadus", "Abram Swiger", "Macy Hinkle", "Marquita Cendejas", "Yolande Olivero", "Shirly Manzo", "Alverta Burges", "Lynwood Sponsler", "Hilton Delreal", "Lynelle Dahlen", "Dorla Tweedy", "Tyesha Draper", "Beckie Degarmo", "Warner Dorsett", "Ernesto Tassin", "Victoria Lal", "Latoya Smelcer", "Natalia Santerre", "Jodie Lieu", "Barton Darcangelo", "Neda Maza", "Lana Tippin", "Caron Melcher", "Easter Renner", "Amparo Pilot", "Lucinda Tolley"]


my_verein = Verein('My Verein')

for name in names[:10]:
    my_verein.mitgliedHinzufuegen(name)

my_verein.vorstandWaehlen()

print(my_verein.mitglieder)
print(my_verein.vorstand)

my_verein.delMitglied()
print(my_verein.mitglieder)
