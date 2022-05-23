#Calculando descontos:

precoProduto = float(input(' Valor do produto: '))
valorProdcomDesc = precoProduto - (precoProduto * 5 / 100)
print(' O produto que custava {}, com desconto de 5% vai custar {:.2f}'.format(precoProduto, valorProdcomDesc))