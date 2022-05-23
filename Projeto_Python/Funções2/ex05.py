# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# -A maior nota
# -A menor nota
# -A média da turma
# -A situação(Opcional)


def notas(*n, situacao=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)# pega total de notas, soma e divide o resultado da soma pela quantidade de notas
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r

#Programa Principal
resp = notas(9, 10, 5.5, 2.5, 8.5, situacao=True)
print(resp)
help(notas)
