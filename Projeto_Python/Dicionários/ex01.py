# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

#media valor1 + valor2 /2

aluno = {'nome':str(input("Nome do aluno: "))}
aluno['media']= float(input(f"média de {aluno['nome']}: "))
if aluno['media']>= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for keey, valuee in aluno.items():
    print(f'-{keey} = {valuee}')
