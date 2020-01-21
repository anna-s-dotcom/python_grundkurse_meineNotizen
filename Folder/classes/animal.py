class Lebewesen:
    def __init__(self, ld, g):
        self.lebensdauer = ld
        self.gewicht = g

    def __str__(self):
        return f'Lebensdauer: {self.lebensdauer} Jahre\nGewicht: {self.gewicht}kg'
