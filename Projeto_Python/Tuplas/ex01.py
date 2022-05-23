# Crie um programa que tenha uma tupla totalmente
# preenchida com uma contagem por extenso, de 0 até 20.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostra-lo por extenso.

cont = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ"
            "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", 
            "DEZENOVE", "VINTE")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número {cont[num]}")