# while True:
# z=input("Zahl eingeben")
# if zahl.isdigit():
#     break
# else:
#     print("Falsche Eingabe")
#
# print("End of programm")
#
#
# z=input("Zahl eingeben")
# try:
#     z=0
#     z=int(z)
# except Exception as e:
#     print(e)
#     print(type(e))

#er sagt was man machen sollte, programm nicht abbricht

while True:
    zahl=input("Zahl eingeben: ")
    try:
        zahl=float(zahl)
        break
    except:
        print("Falsche Eingaben")
print(zahl+589)
