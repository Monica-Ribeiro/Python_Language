# Crie um programa que leia o ano de nascimento de 
# sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas ja são maiores.
from datetime import date
atual = date.today().year
totalMaior = 0
totalmenor = 0
for pessoa in range(1,8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu ? ".format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        totalMaior = totalMaior + 1
    else:
        totalmenor = totalmenor + 1
print("Ao todo tivemos {} pessoas já atingiram a maioridade.".format(totalMaior))
print("E também tivemos {} pessoas ainda não atingiram a maioridade.".format(totalmenor))
