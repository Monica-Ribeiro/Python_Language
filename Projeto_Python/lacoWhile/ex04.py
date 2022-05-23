# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# EX: 5! = 5 x 4 x 3 x 2 x 1 = 120


numero = int(input("Digite um número para calcular o seu fatorial: "))
c = numero
f = 1
print("Calculando {}! = ".format(numero), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" X " if c > 1 else " = ", end="")
    f = f * c
    c = c - 1
print("{}".format(f))


# OUTRA FORMA DE FAZER ESSE EXERCICIO SEM WHILE:
# from math import factorial
# n = int(input("Digite um número para calcular o seu fatorial: "))
# f =factorial(n)
# print("O fatorial de {} é {}.".format(n, f))
