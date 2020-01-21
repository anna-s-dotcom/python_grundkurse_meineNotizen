def is_number(n):
    try:
        float(n)
        return True
    except:
        return False

while True:
    e = input('Zahl: ')
    if is_number(e):
        break
    else:
        print('wrong!')

e = input('Zahl: ')
while not is_number(e):
    e = input('Zahl: ')

e = input('Zahl: ')
while is_number(e) == False:
    e = input('Zahl: ')
