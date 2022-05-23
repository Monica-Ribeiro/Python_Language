# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média
from time import sleep
galera = list()
pessoa = dict()
soma = 0
media = 0
while True:
    pessoa.clear()# esvaziar pessoa pq vai vir uma pessoa nova
    pessoa['Nome'] = str(input("Nome: "))
    while True:
        pessoa['Sexo'] = str(input("Sexo: ")).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['Idade'] = int(input('Idade: '))
    soma = soma + pessoa["Idade"]
    galera.append(pessoa.copy())# galera recebe uma cópia de pessoa.
    while True:
        resposta = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resposta in "SN":
            break
        print("ERRO! Digite apenas S ou N.")
    if resposta == "N":
        break
print("-=" * 30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A média de idade é de {media:5.2f} anos.")

print("C) As mulheres cadastradas foram ", end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()#quebra de linha depois do resultado do print das mulheres cadastradas.
print ("D) Lista de pessoas que estão com idade acima da média: ")
for p in galera:
    if p['Idade'] >= media:
        print('     ', end='')
        for keey, valuee in p.items():
            print(f"{keey} = {valuee}; ", end='')
print()#quebra de linha
print("<< ENCERRADO >>")
