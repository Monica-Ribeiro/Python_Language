# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numero = []
for cont in range(0, 5):
     numero.append(int(input(f"Digite um número na posição {cont}: ")))
     if cont == 0:
         maior = menor = numero[cont]
     else:
         if numero[cont] > maior:
             maior = numero[cont]
         if numero[cont] < menor:
             menor = numero[cont]
print("-=" * 30)
print(f"Você digitou os valores {numero}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for posicao, v in enumerate(numero):
    if v == maior:
        print(f"{posicao}.", end="")
print()
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for posicao, v in enumerate(numero):
    if v == menor:
        print(f"{posicao}.", end="")
