# Melhore o exercicio onde o computador vai "pensar" um número de 0 a 10,
# só que agora o jogador vai adivinhar até acertar, mostrando no final
# quantos palpites foram nescessários para vencer.

 # Advinhação:

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10.')
print("Será que você consegue adivinhar qual foi ? ")
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite ? "))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
print("Acertou com {} tentativas. Parabéns!".format(palpites))