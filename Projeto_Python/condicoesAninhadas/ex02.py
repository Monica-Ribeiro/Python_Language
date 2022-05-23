#Escreva um programa que leia um número inteiro qualquer e peça
#para o usuário escolher a base de convrsão.

numero = int(input("Digite um número:"))
print("""Escolha a base que deseja fazer a conversão:
         [1] - Converter para Binário
         [2] - Converter para Octal
         [3] - Converter para Hexadecimal """)
baseConversao = int(input("Sua opção: "))
if baseConversao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(numero, bin(numero) [2:]))
elif baseConversao == 2:
    print("{} convertido para OCTAL é igual a {}".format(numero, oct(numero) [2:]))
elif baseConversao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(numero, hex(numero) [2:]))
else:
    print("Número invalido!")
