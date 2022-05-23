# Crie uma tupla preenchida com os 20 primeiros colocados
# da tabela do campeonato brasileiro de futebol, na ordem
# de colocação. Depois mostre:
# A - Apenas os 5 primeiros colocados.
# B - Os últimos 4 colocados da tabela.
# C - Uma lista com os times em ordem alfabética.
# D - Em que posição na tabela está o time da Chapecoense.

times = (   "Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro",
            "Flamengo", "Vasco", "Chapecoense", "Atlético", "Botafogo",
            "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife",
            "EC Vitória", "Curitiba", "Avai", "Ponte Preta", "Atlético-GO")

print("Lista de times: {}".format(times))
print("-=" * 60)
print(f"Os 5 primeiros times colocados são: {times[0:5]}")
print("-=" * 60)
print(f"Os 4 últimos são: {times[-4:]}")
print("-=" * 60)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 60)
print(f"O time do Chapecoense está na {times.index('Chapecoense') + 1}ª posição.")