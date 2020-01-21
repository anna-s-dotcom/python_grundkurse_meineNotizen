# def plus5(x):
#      return (x+5)
#
#
# y=plus5(5)
#
# z=plus5(444)
#
# print(y)
# print(z)
#
# def summe(x,y):
#     return x+y
#
# y= summe(z,6)
# print(y)
#
#
# z=summe("Hello", "World!")
#
# print(z)
#
# def spacer():
#     print("________________")
#
# spacer()
#
# def summe2(x=5, y=10):
#     return x+y
#
# print("summe2()")
# print(summe2())
# print("summe2(10)")
# print(summe2(10))
# print("summe2(y=20)")
# print(summe2(y=20))
#
# import random
#
# #erstellt eine zahl zwischen 1 und 5 (incl 1 und 5)
# print(random.randint(1,5))

#erstelle eine Funktuin, welche den Abstand
#zwischen zwei Zahlen ermittel
#der Abstand ist die differenz der zwei zahlen, aber immer positiv
#berechne den Abstand zwischen zwei zufälligen zahlen
#bonus: berechne zehn abstände zwischen je zwei zufälligen Zahlen

#mein lösung war es_________________
# x=int(input("Gib x ein"))
# y=int(input("Gib y ein"))
#
# def abstand(x,y):
#         return x-y
#
# while x>y:
#
#     print()

#_____________

x=random.randint(1,10)
y=random.randint(1,10)

def my_betrag(a,b)
    if a>=b:
        return a-b
    else:
        my_betrag(b,a)

def my_betrag2(a,b):
    c=a-b
    if c>0:
        return c
