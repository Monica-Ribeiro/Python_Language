# Crie um programa que vai gerar 5 números aleatórios
# e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))
print("Os valores sorteados foram: ", end="")
for n in numeros:
    print(f"{n} ")
print(f"O maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")