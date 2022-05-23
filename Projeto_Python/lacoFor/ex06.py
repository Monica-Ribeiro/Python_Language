# Desenvolva um programa que leia o primeiro termo de uma PA (Progressão Aritmética).
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for cont in range(primeiro, decimo + razao, razao):
    print("{}".format(cont), end="-")
print("ACABOU")