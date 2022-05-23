# Crie uma tupla única com nomes de produtos, e seus respectivos
# preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados de forma tabular.

produtos = ("Lápis", "1.75", "Borracha", "2.00", "Caderno", "15.00", "Estojo", "25.00",
                "Transferidor", "4.20", "Compasso", "9.99", "Mochila", "120.00", "Canetas", "22.30", "Livro", "34.90")

print("-=" * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-=" * 20)
for p in range(0, len(produtos)):
    if p % 2 == 0:
       print(f"{produtos[p]:.<30}",end="")
    else:
        print(f"R${produtos[p]:>7}")
print("-=" * 20)