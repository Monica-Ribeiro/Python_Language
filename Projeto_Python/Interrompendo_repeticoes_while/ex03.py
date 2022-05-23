# Faça um programa que jogue par ou impar com o computador.
# O jogo será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print("-=" * 30)
print("VAMOS JOGAR PAR OU IMPAR")
print("-=" * 30)
cont = 0
soma = 0
escolha = ""
while True:
    computador = randint(0, 10)
    jogador = int(input("Diga um valor: "))
    escolha = str(input("PAR ou ÍMPAR ? [P/I] ")).strip().upper()[0]
    soma = jogador + computador
    print("Você jogou {} e o computador {}. Total de {}".format(jogador, computador, soma))
    print("DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR")
    if escolha in "Pp":
        if soma % 2 == 0:
            print("VOCÊ VENCEU!")
            soma = soma + 1
            cont = cont + 1
        else:
            print("VOCÊ PERDEU!")
            print("GAME OVER!!!")
            break
    elif escolha in "Ii":
        if soma % 2 == 1:
            print("VOCÊ VENCEU")
            soma = soma + 1
            cont = cont + 1
        else:
            print("VOCÊ PERDEU!")
            print("GAME OVER!!!")
            break
        print("Vamos jogar novamente...")
print("Você venceu {} vezes".format(cont))
