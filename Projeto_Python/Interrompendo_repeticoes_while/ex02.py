# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

# tabuada = int(input('Digite um numero para exibir a tabuada:'))
# print('Tabuada do numero:',tabuada)
# for valor in range(1,11,1):
#     print(str(tabuada) + 'X' + str(valor) + '=' + str(tabuada*valor))


while True:
    tabuada = int(input("Digite um número para exibir a tabuada: "))
    if tabuada < 0:
        break
    print("-=" * 30)
    for cont in range(1,11):
        print(str(tabuada) + 'X' + str(cont) + '=' + str(tabuada*cont))
    print("-=" * 30)
print("Fim do programa!")