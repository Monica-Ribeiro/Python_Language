# Ordem de precedencia:

n1 = int(input('Um número:'))
n2 = int(input('Outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2
print('A soma é: {}, o produto é: {} e a divisão é: {:.3f}'.format(s, m, d))
print('Divisão inteira: {} e a potência:{}'.format(di, exp))