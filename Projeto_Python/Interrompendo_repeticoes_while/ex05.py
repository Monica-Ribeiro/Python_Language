# Crie um programa que que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A- qual é o total gasto na compra.
# B- Quantos produtos custam mais de 1000.
# C- Qual é o nome do produto mais barato.

maiorValor = 0
menorValor = 0
prodBarato = " "
cont = 0
total = 0
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço do produto: "))
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        maiorValor = maiorValor + 1
    if cont == 1:
        menorValor = preco
        prodBarato = produto
    else:
        if preco < menorValor:
            menorValor = preco
            prodBarato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar ? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print("{:-^40}".format("FIM DO PROGRAMA!"))
print("O total da compra foi R$ {:2.2f}".format(total))
print("Temos {} produtos custando mais de R$ 1000.00".format(maiorValor))
print("O produto mais barato foi {} que custa R$ {:.2f}".format(prodBarato, menorValor))