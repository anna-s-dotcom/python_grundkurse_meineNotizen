if __name__ == '__main__':
    from animal import Lebewesen
else:
    from classes.animal import Lebewesen

class Bird(Lebewesen):
    def __init__(self, ld2, g2, ef, sz):
        # super().__init__(ld2, g2)
        Lebewesen.__init__(self, ld2, g2)
        self.eierfarbe = ef
        self.schlupfzeit = sz

    def __str__(self):
        return f"Lebensdauer: {self.lebensdauer} Jahre\nEierfarbe: {self.eierfarbe}"
