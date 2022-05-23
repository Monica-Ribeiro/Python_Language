def aumentar(num, taxa):
    res = num + (num * taxa / 100)# add porcentagem em cima do valor.
    return res

def diminuir(num, taxa):
    res =num - (num * taxa / 100)
    return res

def dobro(num):
    res = num * 2
    return res

def metade(num):
    res = num / 2
    return res