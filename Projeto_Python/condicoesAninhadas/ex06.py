# Faça um programa que leia a idade de um atleta e mostre sua categoria,
# de acordo com a idade:
# Até 9 anos: MIRIM, até 14 anos: INFANTIL, até 19 anos: JÚNIOR,
# até 25 anos: SÊNIOR, acima: MASTER
from datetime import date
anoAtual = date.today().year

anoNasc = int(input("Ano de nascimento: "))
idade = anoAtual - anoNasc
print("Quem nasceu em {} tem {} em {}.".format(anoNasc, idade, anoAtual))
if idade <= 9:
    print("Classificação MIRIM")

elif idade > 9 and idade <= 14:
    print("Classificação INFANTIL")

elif idade > 14 and idade <= 19:
    print("Classificação JÚNIOR")

elif idade > 19 and idade <= 25:
    print("Classificação SÊNIOR")

elif idade > 25:
    print("Classificação MASTER")