# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(" X ", end='')
            else:
                print(" = ", end='')
        f *= c
    return f

#Programa principal
print(fatorial(5, show=True))#se inserir o False no lugar do True, será exibido apenas o resultado final (120) ao invés da sequência que aparece antes do resultado final.