import os
from smtpd import MailmanProxy


# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais.

Valor1 = int(input("Digite o primeiro valor: "))
Valor2 = int(input("Digite o segundo valor: "))

if Valor1 > Valor2:
    print("O primeiro valor é maior.")
elif Valor1 < Valor2:
    print("O segundo valor é maior.")
elif Valor1 == Valor2:
    print("Não existe valor maior, os dois são iguais.")
else:
    print("Comando inválido!")