# Crie um programa que leia vários números  inteiros
# pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles(desconsiderando flag).

cont = 0
soma = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print("Foram digitados {} números e a soma entre eles é : {}".format(cont, soma))

#Transformei o laço de repetição em um looping infinito e usei uma condição de parada para interromper o laço.