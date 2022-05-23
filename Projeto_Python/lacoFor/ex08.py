# Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços.
# EX: - Apos a sopa
# - A sacada da casa
# - A torre da derrota
# - O lobo ama o bolo
# - Anotaram a data da maratona

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
        inverso = inverso + junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase não é um palindromo!")

# OUTRA FORMA DE FAZER ESSE EXERCICIO UTILIZANDO SÓ CONDICIONAL:
# frase = str(input("Digite uma frase: ")).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = junto[::-1]
# print("O inverso de {} é {}".format(junto, inverso))
# if inverso == junto:
#     print("Temos um palíndromo!")
# else:
#     print("A frase não é um palindromo!")