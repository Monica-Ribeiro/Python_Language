# Faça um programa que mostre o nome completo de uma pessoa e mostre separadamente
# o primeiro e o último nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!'.format(nome))
nome = nome.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))