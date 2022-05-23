# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import arquivoEx01

num = float(input("Digite um valor: "))
print(f"A metade de R$ {num} é {arquivoEx01.metade(num)}")
print(f"O dobro de R$ {num} é {arquivoEx01.dobro(num)}")
print(f"Aumentando 10%, temos R$ {arquivoEx01.aumentar(num, 10)}")
print(f"Reduzindo 13%, temos {arquivoEx01.diminuir(num, 13)}")