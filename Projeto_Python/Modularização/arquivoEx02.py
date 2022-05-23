def aumentar(num=0, taxa=0):
    res = num + (num * taxa / 100)# add porcentagem em cima do valor.
    return res

def diminuir(num=0, taxa=0):
    res = num - (num * taxa / 100)
    return res

def dobro(num=0):
    res = num * 2
    return res

def metade(num=0):
    res = num / 2
    return res

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:>.2f}'.replace('.', ',')