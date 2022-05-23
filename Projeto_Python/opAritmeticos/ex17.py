# Sorteando uma ordem na lista:
from random import shuffle
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

# Outro exemplo:
#import random
#aluno1 = str(input('Primeiro aluno: '))
#aluno2 = str(input('Segundo aluno: '))
#aluno3 = str(input('terceiro aluno: '))
#aluno4 = str(input('Quarto aluno: '))
#lista = [aluno1, aluno2, aluno3, aluno4]
#random.shuffle(lista)
#print('A ordem de apresentação será: {}'.format(lista))