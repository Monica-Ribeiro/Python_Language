# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5: abaixo do peso
# -Entre 18.5 e 25: peso ideal
# -25 até 30: sobrepeso
# -30 até 40: obesidade
# -Acima de 40: obesidade mórbida

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (M) "))
imc = peso /(altura ** 2)
print(" O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está no peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 40:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")