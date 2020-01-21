
# Erstelle die Klassen Lebewesen, Säugetier, Vogel
# Klasse Lebewesen: Attribute: Lebensdauer, Gewicht
# Klasse Säugetier: Attribute: Lebensdauer, Gewicht, Tragezeit, Säugezeit
# Klasse Vogel: Attribute: Lebensdauer, Gewicht, Schlüpfzeit, Eierfarbe
#
# 1) Erstelle die Klasse Lebewesen

class Lebewesen:
    def __init__(self, ld, g):
        self.lebensdauer = ld
        self.gewicht = g

    def __str__(self):
        return f'Lebensdauer: {self.lebensdauer} Jahre\nGewicht: {self.gewicht}kg'

hund = Lebewesen(18, 12)
print(hund)
print()
# 2) Erstelle die Klassen Säugetier Vogel als Child von Lebewesen

class Mammal(Lebewesen):
    def __init__(self, ld1, g1, tz1, sz1):
        # super().__init__(ld1, g1)
        Lebewesen.__init__(self, ld1, g1)
        self.tragzeit = tz1
        self.saugzeit = sz1

    def __str__(self):
        return Lebewesen.__str__(self) + f"\nTragezeit: {self.tragzeit} Monate"

class Bird(Lebewesen):
    def __init__(self, ld2, g2, ef, sz):
        # super().__init__(ld2, g2)
        Lebewesen.__init__(self, ld2, g2)
        self.eierfarbe = ef
        self.schlupfzeit = sz

    def __str__(self):
        return f"Lebensdauer: {self.lebensdauer} Jahre\nEierfarbe: {self.eierfarbe}"

katze = Mammal(14, 5, 6, 0.5)
print(katze)
print()
pinguin = Bird(6, 9, 'gepsprenkelt', 12)
print(pinguin)
print()
# 3) Erstelle die Klasse Schnabeltier als Child von Säugetier und Vogel

# geht nur mit zeile 24, 34 auskommentiert

class Platypus(Mammal, Bird):
    def __init__(self, ld3, g3, ef, schlupfz, saugzz):
        Mammal.__init__(self, ld3, g3, tz1 = 0, sz1 = saugzz)
        Bird.__init__(self, ld3, g3, ef, schlupfz)

    def __str__(self):
        return super().__str__() + f"\nSäugezeit: {self.saugzeit}"

platy = Platypus(5, 7, 'gelb', 5, 6)
print(platy)
