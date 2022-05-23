# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108
from arquivoEx03 import *


num = float(input('Digite o preço: R$'))

print(f'A metade de {moeda(num)} é {moeda(metade(num))}')
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'Aumentando 10% nós temos {moeda(aumentar(num, 10))}')
print(f"Reduzindo 13%, temos {moeda(diminuir(num, 13))}")