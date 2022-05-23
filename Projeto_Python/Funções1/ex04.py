# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*num):
    for valor in num:
        print(f"{valor} ", end='')
    print(f"O maior valor é {max(num)}")

maior(2,9, 4, 5, 7, 1)
maior(4, 7,0)
maior(1, 2)
maior(6)