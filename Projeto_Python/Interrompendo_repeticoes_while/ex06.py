# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No inicio, pergunte aos usuários qual será o valor a ser sacado(número inteiro)
# e o programa vai informar quantas células de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("=" * 40)
print("{:^40}" .format("BANCO MR"))
print("=" * 40)
valor = int(input("Que valor você deseja sacar ? R$ "))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        totalCedula = totalCedula + 1
    else:
        if totalCedula > 0:
            print("Total de {} cédulas de R$ {}".format(totalCedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print("=" * 40)
print("{:^40}" .format("Volte sempre ao BANCO MR! Tenha um bom dia!"))
print("=" * 40)