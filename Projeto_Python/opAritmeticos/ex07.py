# Convertendo real em dólar:

real = float(input(' Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.23
print('Com R$ {:.2f} você pode comprar US${:.2f} dólares.'.format(real, dolar))