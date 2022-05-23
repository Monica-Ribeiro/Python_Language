# Crie um programa que que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A- quantas pessoas tem mais de 18 anos.
# B- quantos homens foram cadastrados.
# C- Quantas mulheres tem menos de 20 anos.
maior18 = 0
totalHomem = 0
totalMulher20 = 0
print("-=" * 30)
print("CADASTRE UMA PESSOA")
print("-=" * 30)
while True:
    idade = int(input("Idade: "))
    if idade <= 18:
        maior18 = maior18 + 1
    sexo = str(input("Sexo: [F/M] ")).strip().upper()[0]
    while sexo not in "MmFf":
        print("ERRO!!! Digite apenas M ou F. Tente novamente: ")
        sexo = str(input("Sexo: [F/M] ")).strip().upper()[0]
    if sexo == "M":
        totalHomem = totalHomem + 1
    if sexo == "F" and idade < 20:
        totalMulher20 = totalMulher20 + 1
    resposta = str(input("Quer continuar ? [S/N] ")).strip().upper()[0]
    while resposta not in "SsNn":
        print("ERRO!!! Digite apenas S ou N. Tente novamente: ")
        resposta = str(input("Quer continuar ? [S/N] "))
    if resposta in "N":
        break
print("Total de pessoas com mais de 18 anos: {}".format(maior18))
print("Ao todo temos {} homens cadastrados.".format(totalHomem))
print("Temos {} mulheres com menos de 20 anos.".format(totalMulher20))