# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numero = list()
pares = list()
impares = list()
while True:
    numero.append(int(input("Digite um número: ")))
    resposta =str(input("Quer continuar ? [S/N] "))
    if resposta in "Nn":
        break
for indice, valor in enumerate(numero):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print("-=" * 30)
print(f"A lista completa é: {numero}")
print(f"A lista de pares é: {pares}")
print(f"A lsta de impares é: {impares}")