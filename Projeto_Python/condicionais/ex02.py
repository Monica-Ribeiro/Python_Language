# Radar eletrônico:

velocidade = float(input('Qual a velocidade percorrida? '))
if velocidade > 80:
    print('Multado! a velocidade percorrida estava acima de 80km/h.')
    multa = (velocidade-80) * 7
    print('A multa vai ser de: R${:.2f}.'.format(multa))
else:
    print('Tenha um bom dia! dirija com segurança.')