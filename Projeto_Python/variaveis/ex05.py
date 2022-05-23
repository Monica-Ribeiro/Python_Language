# Dissecando uma variavel:

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(a)))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Esta em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizado? ', a.istitle())
