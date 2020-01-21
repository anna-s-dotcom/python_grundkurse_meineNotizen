class Lebenswesen:
    def __init__(self, lebensdauer, gewicht):
        self.lebensdauer = lebensdauer
        self.gewicht = gewicht

    def __str__(self):
        return f"Lebenswesen - Lebensdauer: {self.lebensdauer}, Gewicht {self.gewicht}"

animal1=Lebenswesen("50", "65")
print(animal1)

class Saeugetier(Lebenswesen):
    def __init__(self,lebensdauer, gewicht, tragezeit,saegezeit):
        Lebenswesen.__init__ (self,lebensdauer, gewicht)
        self.tragezeit=tragezeit
        self.saegezeit=saegezeit


    def __str__(self):
        return f"Saugetier - Lebensdauer: {self.lebensdauer}Jahre, Gewicht: {self.gewicht} kg, Tragezeit:{self.tragezeit} Monate, Sägezeit:{self.saegezeit} Monate"

mensch=Saeugetier("80","70","9","24")
print(mensch)

class Vogel(Lebenswesen):
    def __init__(self, lebensdauer,gewicht, schluepfezeit, eierfarbe):
        Lebenswesen.__init__ (self,lebensdauer, gewicht)
        self.schluepfezeit=schluepfezeit
        self.eierfarbe=eierfarbe

    def __str__(self):
        return f"Vogel - Lebensdauer: {self.lebensdauer} Jahre, Gewicht: {self.gewicht} kg, schluepfezeit: {self.schluepfezeit} Monate, Eierfarbe: {self.eierfarbe}"

taube=Vogel("2","5","2","weiß")
print(taube)

class Schnabeltier(Saeugetier,Vogel):
    def __init__(self, lebensdauer,gewicht, schluepfezeit, eierfarbe,tragezeit,saegezeit):
        Vogel.__init__(self, lebensdauer, gewicht,schluepfezeit, eierfarbe)
        Saeugetier.__init__(self,lebensdauer, gewicht,tragezeit,saegezeit)

    def __str__(self):
        return f"Vogel - Lebensdauer: {self.lebensdauer} Jahre, Gewicht: {self.gewicht} kg, schluepfezeit: {self.schluepfezeit} Monate, Eierfarbe: {self.eierfarbe} Tragezeit:{self.tragezeit} Monate, Sägezeit:{self.saegezeit} Monate"

tier1=Schnabeltier("12","60","12","blau","6","5")
print(tier1)
