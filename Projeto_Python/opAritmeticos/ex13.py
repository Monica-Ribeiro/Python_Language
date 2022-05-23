# Transformando em inteiro números quebrados:

from math import trunc
import math
numero = float(input('Digite um número: '))
print('O valor digitado foi: {} e a sua porção inteira é: {}.'.format(numero,  math.trunc(numero)))

#Outro exemplo de quebrar um numero:
#numero = float(input('Digite um número: '))
#print('O valor digitado é: {} e sua porção inteira é: {}.'.format(numero, int(numero)))