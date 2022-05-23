# Escreva um programa que leia um número inteiro qualquer
# e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
# EX: 0-1-1-2-3-5-8


print("-=" * 30)
print("Sequência de fibonacci")
print("-=" * 30)
numero = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print("~" * 30)
print("{} - {}".format(t1, t2), end="")
cont = 3
while cont <= numero:
    t3= t1 + t2
    print(" - {}".format(t3), end="")
    t1 = t2
    t2 = t3
    cont = cont + 1
print(" - FIM")
print("~" * 30)