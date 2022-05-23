# Crie um programa que leia vários números  inteiros
# pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles(desconsiderando flag).
num = 0
cont = 0
soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num !=  999:
    soma = soma + num
    cont = cont + 1
    num = int(input("Digite um número [999 para parar]: "))
print("Foram digitados {} números e a soma entre eles é : {}".format(cont, soma))
