# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]Somar
# [2]Multiplicar
# [3]Maior
# [4]Novos números
# [5]Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
menu = 0
while menu != 5:
    print("""------------MENU--------------
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior número
        [4] - Novos números
        [5] - Sair do programa""")
    menu = int(input(">>>>>> Qual operação você deseja realizar ? "))
    if menu == 1:
        soma = (valor1 + valor2)
        print("A soma entre {} e {} é: {}".format(valor1, valor2, soma))
    elif menu == 2:
        multiplicar = (valor1 * valor2)
        print("A multiplicação entre {} e {} é: {}".format(valor1, valor2, multiplicar))
    elif menu == 3:
        if valor1 > valor2:
            maiorValor = valor1
        else:
            maiorValor = valor2
            print("Entre {} e {} o maior valor é: {}".format(valor1, valor2, maiorValor))
    elif menu == 4:
        print("informe os números novamente: ")
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    elif menu == 5:
        print("Finalizando...")
    else:
        print("Opção inválida! tente novamente:")
    print("=-=" * 10)
    sleep(2)
print("Fim do programa! Volte sempre!")