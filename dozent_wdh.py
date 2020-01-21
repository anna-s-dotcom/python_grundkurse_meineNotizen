import random

class Parent:
    def __init__(self, name1, name2):
        self.vorname = name1
        self.nachname = name2
        self.age = random.randint(22, 45)

    def geburtstag(self):
        self.age += 1

    def __str__(self):
        return f"{self.vorname} {self.nachname}, {self.age}"


class Child(Parent):
    def __init__(self, name, parent1, parent2):
        # super().__init__(name, parent1.nachname)
        # Parent.__init__(self, name, parent1.nachname)
        self.mutter = parent1
        self.vater = parent2
        self.vorname = name
        if self.vater.nachname == self.mutter.nachname:

        else:
            self.nachname = self.mutter.nachname + "-" + self.vater.nachname
        self.age = random.randint(4, 9)

p1 = Parent('Heide', 'Müller')
p2 = Parent('Gert', 'Meier')

print(p1)
print(p2)

child = Child('Erwin', p1, p2)
# child = Child(name = 'Erwin', parent1 = p1, parent2 = p2)

print(child)
child.geburtstag()
print(child)

print(child.vater)

print(type(p2))
print(type(child.vater))

# names = [('Heide', 'Müller'), ('Gert', 'Müller')]
# parents = []
# for name in names:
#     parent = Parent(name[0], name[1])
#     parents.append(parent)
# for parent in parents:
#     print(parent)

# parents = [Parent(name[0], name[1]) for name in names]
# for parent in parents:
#     print(parent)
