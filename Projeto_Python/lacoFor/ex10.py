# Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e qual foi o menor peso lidos.
pesoMaior = 0
pesoMenor = 0
for pessoa in range(1,6):
    peso = float(input("Peso da {}ª pessoa: ".format(pessoa)))
    if pessoa == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print("O maior peso lido foi de {}Kg".format(pesoMaior))
print("O menor peso lido foi de {}Kg".format(pesoMenor))