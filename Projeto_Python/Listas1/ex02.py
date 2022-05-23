# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

numero = []

while True:
    num = int(input("Digite um valor: "))
    if num not in numero:
        numero.append(num)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado, não vou adicionar.")
    resposta= str(input("Quer conituar ?  [S/N] "))
    if resposta in "Nn":
        break
print("-=" *30)
numero.sort()
print(f"Você adicionou os valores {numero}")