# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
total = int(input(f'Qauntas partidas {jogador["Nome"]} jogou ?'))
for cont in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {cont} ? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print("-=" * 30)
print(jogador)
print("-=" * 30)
for keey, valuee in jogador.items():
    print(f'O campo {keey} tem o valor {valuee}')
print("-=" * 30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols')