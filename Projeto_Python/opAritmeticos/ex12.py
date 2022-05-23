# Aluguel de carros:

dias = int(input('Quantos dias ficou alugado? '))
km = float(input('Quantos km rodados? '))
valorPagar = (dias * 60) + (km * 0.15)
print('O total a pagar é: R$ {}'.format(valorPagar))
