# while True:
#     z = input('Zahl eingeben: ')
#     if z.isdigit():
#         break
#     else:
#         print('Falsche Eingabe!')
#
# print('end of program')

# z = input('Zahl eingeben: ')
#
# try:
#     s = 5
#     z = int(z)
# except Exception as e:
#     print(e)
#     print(type(e))
# print(s)
# print('end of program')


while True:
    zahl = input('Zahl eingeben: ')
    try:
        zahl = float(zahl)
        break
    except:
        print('fasche eingabe')

print(zahl + 564)
