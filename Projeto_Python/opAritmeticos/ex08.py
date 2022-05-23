# Faça um programa que leia a largura e a altura de uma parede em metros
#calcule sua aréa e a quantidade de tinta nescessária para pintá-la
#sabendo que cada litro de tinta pinta 2m quadrados

larg = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = larg * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua aréa é de {}m.'.format(larg, altura, area))
print('Para pintar essa parede, você vai precisar de {} litros de tinta.'.format(tinta))