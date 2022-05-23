# Aprimore o desafio 04 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Qauntas partidas {jogador["Nome"]} jogou ?'))
    partidas.clear()
    for cont in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {cont+1} ? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input("Quer continuar ? [S/N] ")).upper()[0]
        if resposta in 'SN':
            break
        print("ERRO! Responda apenas S ou N.")
    if resposta == 'N':
        break
print("-=" * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
    print()
print("-" * 60)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values:
        print(f'{str(d):>15}', end='')
    print()
print("-=" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador ? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador com código {busca}')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f"    No jogo {i+1} fez {g} gols.")
    print("-=" * 40)
print("<< VOLTE SEMPRE >>")