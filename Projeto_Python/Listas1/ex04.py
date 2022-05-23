# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso
# mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numero = []

while True:
    numero.append(int(input("Digite um valor: ")))
    resposta=str(input("Quer continuar? [S/N] "))
    if resposta in "Nn":
        break
print("-=" * 30)
print(f"Essa lista tem {len(numero)} números")
numero.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {numero}")
if 5 in numero:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
