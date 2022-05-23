# Melhore o desafio 05 da PA(Progressão Aritmética)
# perguntando se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

print("Gerador de  PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} - ".format(termo), end="")
        termo = termo + razao
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer demonstrar a mais ? \n"))
print("Progressão finalizada com {} termos mostrados.".format(total))
print("FIM")