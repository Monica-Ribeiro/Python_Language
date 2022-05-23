#Calculando reajuste salarial:

salario = float(input('Qual é o salário do funcionário?R$ '))
reajuste = salario + (salario * 15 / 100)
print('Um funciorário que ganhava R$ {}, com 15% de aumento, passa a receber {:.2f}.'.format(salario, reajuste))