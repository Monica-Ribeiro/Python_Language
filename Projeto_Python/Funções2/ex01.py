# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

anoAtual = date.today().year
def voto(anoNasc):
    idade = anoAtual - anoNasc
    print(f"Quem nasceu em {Nasc} tem {idade} anos em {anoAtual}.")
    if idade <= 15:
        return "Você é menor de idade, voto negado!"
    elif idade >= 16 and anoNasc < 18:
        return "O voto é opcional!"
    elif idade >= 18:
        return "O voto é obrigatório!"



Nasc = int(input("Digite o ano de nascimento: "))
print(voto(Nasc))