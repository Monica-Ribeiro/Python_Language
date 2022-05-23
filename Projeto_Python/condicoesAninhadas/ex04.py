# Faça um programa que leia o ano de nascimento de um jovem e informe
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 
from datetime import date
anoAtual = date.today().year

anoNasc= int(input("Digite seu ano de nascimento: "))
idade = anoAtual - anoNasc
print("Quem nasceu em {} tem {} em {}.".format(anoNasc, idade, anoAtual))
if idade == 18:
    print("Você tem que se alistar imediatamente!!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento.".format(saldo))
    ano = anoAtual + saldo
    print("Seu alistamento será em {} anos.".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você ja deveria ter se alistado a {} anos!".format(saldo))
    ano = anoAtual - saldo
    print("Seu alistamento foi em {}".format(ano))
else:
    print("Comando inválido!")