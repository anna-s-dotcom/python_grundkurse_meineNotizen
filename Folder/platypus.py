from classes.mammal import Mammal
from classes.bird import Bird
from classes.animal import Lebewesen


class Platypus(Mammal, Bird):
    def __init__(self, ld3, g3, ef, schlupfz, saugzz):
        Mammal.__init__(self, ld3, g3, tz1 = 0, sz1 = saugzz)
        Bird.__init__(self, ld3, g3, ef, schlupfz)

    def __str__(self):
        return super().__str__() + f"\nSäugezeit: {self.saugzeit}"

platy = Platypus(5, 7, 'gelb', 5, 6)
print(platy)
