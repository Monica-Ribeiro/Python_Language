# Calculando custo da viajem:

distancia = float(input('Qual a distancia da viagen em km? '))
print('Você está prestes a realizar uma viajem de {}km.'.format(distancia))
if distancia <= 200:
    passagem = distancia * 0.50
    print('E o preço da sua passagen será de: {:.2f}'.format(passagem))
else:
    passagem = distancia * 0.50
    print('E o preço da sua passagem será de: {:.2f}'.format(passagem))