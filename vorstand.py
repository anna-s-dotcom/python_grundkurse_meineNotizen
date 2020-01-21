import random

class Verein:
    def __init__(self, name):
        self.name = name
        self.vorsitz = None
        self.vorstand=[]
        self.mitglieder=[]

    def mitgliedHinzufuegen(self,m):

        self.mitglieder.append(m)

    def vorstandWaehlen(self,m):
        self.vorstand.append(m)

    def __str__(self):
        return f"Verein {self.name} Vorstand {self.vorstand} Mitglieder: {self.mitglieder}"

my_verein=Verein("Mein Verein")

names=["Jan", "Robert", "Jana"]
vorstand=random.sample(names,2)

for name in names:
    my_verein.mitgliedHinzufuegen(name)

print(my_verein.mitglieder)

for name in vorstand:
    my_verein.vorstandWaehlen(name)

print(my_verein.vorstand)

print(my_verein)
