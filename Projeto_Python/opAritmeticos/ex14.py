# Calculando o cateto da hipotenusa:
from math import hypot
catetoOposto = float(input('Cumprimento do cateto oposto: '))
catetoAdjascente = float(input('Cumprimento do cateto adjascente: '))
catetoHipotenusa = hypot(catetoOposto, catetoAdjascente)
print('A hipotenusa vai medir: {:.2f}'.format(catetoHipotenusa))

#Outro exemplo de como fazer essa operação:
#from math import hypot
#catetoOposto = float(input('Cumprimento do cateto oposto: '))
#catetoAdjascente = float(input('Cumprimento do cateto adjascente: '))
#catetoHipotenusa = (catetoOposto ** 2 + catetoAdjascente ** 2) ** (1/2)
#print('A hipotenusa vai medir: {:.2f}'.format(catetoHipotenusa))