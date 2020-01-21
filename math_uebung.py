#erstelle zwei 4*4 Matrizen mit zufälligen Zahlen
#erstelle eine Matrix, welche in jedem Element das Porduktder anderen Matrizen hat

import numpy as np

m1=np.random.randint(1,11, (4,4))
m2=np.random.randint(1,11, (4,4))
m3=m1*m2

print(m1)
print()
print(m2)
print()
print(m3)
print()


# a=[[1,2][2,3]]
# b=[[2,4][1,3]]
# c=[[1*2, 2*4],[2*3, 3*3]]
#
# m1=np.array([1,2,2,3]).reshape(3,2)
# m2=np.array([2,1,1,2]).reshape(2,2)
#


#Erstelle eine Matrix, welche durch die Matrizenmultiplikation der ersten beiden entsteht.

m4=m1@m2
print(m4)
