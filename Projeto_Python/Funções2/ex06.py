# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'{msg}')
    print('~' * tamanho)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print('ATÉ LOGO')