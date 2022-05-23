 # Advinhação:

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar!'.format(computador))
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
print('Eu pensei no número {}'.format(computador))
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!!!')
else:
    print('Você não conseguiu advinhar, Eu ganhei!!')