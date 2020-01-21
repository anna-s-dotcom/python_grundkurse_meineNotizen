if __name__ == '__main__':
    from animal import Lebewesen
else:
    from classes.animal import Lebewesen

class Mammal(Lebewesen):
    def __init__(self, ld1, g1, tz1, sz1):
        # super().__init__(ld1, g1)
        Lebewesen.__init__(self, ld1, g1)
        self.tragzeit = tz1
        self.saugzeit = sz1

    def __str__(self):
        return Lebewesen.__str__(self) + f"\nTragezeit: {self.tragzeit} Monate"
