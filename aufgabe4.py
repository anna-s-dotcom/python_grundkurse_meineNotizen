einzahlung=int(input('Gib den Betrag ein'))
#200  euro schein
berechnen=einzahlung//200
rest=einzahlung%200
print(berechnen)
# print(rest)
print(f'200euro {berechnen}')

#100 euro schein
berechnen2=rest//100
rest=rest%100

# print(berechnen2)
print(f'100euro {berechnen2}')

#50 euro schein

berechnen3=rest//50
rest=rest%50

# print(berechnen3)
print(f'50euro {berechnen3}')

#20 euro schein

berechnen4=rest//20
rest=rest%20
print(f'20euro {berechnen4}')


#10 euro schein

berechnen5=rest//10
rest=rest%10
print(f'10euro {berechnen5}')


#10 euro schein
berechnen6=rest//5
rest=rest%5
print(f'5euro {berechnen6}')




# auszahlung=input('Dein Rest ist')
