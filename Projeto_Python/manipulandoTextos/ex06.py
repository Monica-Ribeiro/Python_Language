# Faça um programa que leia uma frase pelo teclado e mostre:
# -Quantas vezes aparece a letra A
# -Em que posição ela aparece pela primeira vez
# -Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A') + 1))
print('A letra A aparece pela última vez na posição {}'.format(frase.rfind('A') + 1))