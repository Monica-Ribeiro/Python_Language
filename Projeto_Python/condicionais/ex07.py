# Calculando salário:

salario = float(input('Qual o salário do funcionário? '))
if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
else:
   novoSalario = salario + (salario * 10 / 100)
print('Quem ganhava R$: {:.2f}, passa a ganhar R$: {:.2f}'.format(salario, novoSalario))