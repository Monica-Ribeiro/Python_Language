# Faça um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50.

# for numero in range(2,51,2):
#     print(numero)
# print("Acabou!")

# Outra maneira de obter o mesmo resultado utilizando condição:

for num in range(1,51,):
    if num % 2 == 0:
        print(num)
print("Acabou!")