# Faça um programa que leia um número e diga se ele é ou não
# um número primo.

total = 0
numero = int(input("Digite um número: "))
for cont in range(1, numero + 1):
    if numero % cont == 0:
        print('\033[34m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print("{}".format(cont), end='')
print("O número {} foi divisível {} vezes".format(numero, total))
if total == 2:
    print("E por isso ele é primo.")
else:
    print("E por isso ele não é primo.")
