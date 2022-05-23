# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temporaria = []
principal = []
maiorPeso = 0
menorPeso = 0
while True:
    temporaria.append(str(input("Nome: ")))
    temporaria.append(float(input("Peso: ")))
    if len(principal) == 0:
        maiorPeso = menorPeso = temporaria[1]
    else:
        if temporaria[1] >maiorPeso:
            maiorPeso = temporaria[1]
        if temporaria[1] < menorPeso:
            menorPeso = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resposta in "Nn":
        break
print("-=" * 30)
print(f"Os dados foram: {principal}")
print(f"Ao todo você cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi de {maiorPeso} Kg. Peso de ", end="")
for p in principal:
    if p[1] == maiorPeso:
        print(f"[{p[0]}]", end=" ")
print()  
print(f"O menor peso foi de {menorPeso} Kg. Peso de ", end="")
for p in principal:
    if p[1] == menorPeso:
        print(f"[{p[0]}]", end=" ")
print()