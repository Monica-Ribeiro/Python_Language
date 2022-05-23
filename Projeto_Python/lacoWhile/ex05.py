# Refaça o desafio da PA(Progressão Aritmética)
# lendo o primeiro termo e a razão de uma PA, mostrando
# os primeiros termos da progressão usando a estrutura while.

print("Gerador de  PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} - ".format(termo), end="")
    termo = termo + razao
    cont = cont + 1
print("FIM")