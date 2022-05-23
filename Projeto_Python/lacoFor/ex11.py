# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final, mostre:
# -A média de idade do grupo
# -Qual é o nome do homem mais velho
# -Quantas mulheres tem menos de 20 anos.
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = 0
totalMulher20 = 0
for pessoa in range(1,5):
    print("======={}ª PESSOA=======".format(pessoa))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaIdade = somaIdade + idade
    if pessoa == 1 and sexo in "Mm":
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in "Mm" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in "Ff" and idade < 20:
        totalMulher20 = totalMulher20 + 1
mediaIdade = somaIdade / 4
print("A média de idade do grupo é de {} anos.".format(mediaIdade))
print("O homem mais velho tem {} anos e se chama {}".format(maiorIdadeHomem, nomeVelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(totalMulher20))