# from io import RawIOBase
# from ssl import MemoryBIO


# Refaça o exercicio da tabuada, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando o laço for.

num = int(input("Digite um número para exibir a tabuada: "))
for cont in range(1, 11):
    print("{} X {} = {}".format(num, cont, num * cont))


# Outra forma de obter o mesmo resultado:
# tabuada = int(input("Digite um número para exibir a tabuada: "))
# print("Tabuada do número: ",tabuada)
# for valor in range(1,11,1):
#      print(str(tabuada) + 'X' + str(valor) + '=' + str(tabuada*valor))