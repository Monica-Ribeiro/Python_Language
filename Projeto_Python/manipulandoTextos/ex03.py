# Faça um programa que leia uma número de 0 até 9999 e mostre na tela cada um dos digitos separados.
# EX: Digite um número:1834
# Unidade:4, Dezena: 3, centena:8, milhar:1

numero = int(input('Digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}...'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(dezena))
print('Milhar: {}'.format(milhar))