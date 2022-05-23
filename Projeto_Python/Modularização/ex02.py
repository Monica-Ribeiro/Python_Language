# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
from arquivoEx02 import *


num = float(input('Digite o preço: R$'))

print(f'A metade de {moeda(num)} é {moeda(metade(num))}')
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'Aumentando 10% nós temos {moeda(aumentar(num, 10))}')
print(f"Reduzindo 13%, temos {moeda(diminuir(num, 13))}")