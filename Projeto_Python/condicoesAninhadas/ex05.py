# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# -Média abaixo de 5.0: REPROVADO
# -Média de 5.0 e 6.9: RECUPERAÇÃO 
# -Média de 7.0 ou superior: APROVADO

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota:"))
media = (nota1 + nota2) / 2
print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(nota1, nota2, media))
if  media >= 5 and media < 7:
    print("Você ficou de recuperação!")
elif media < 5:
    print("Você foi reprovado")
elif media >= 7:
    print("Parabéns, você foi aprovado!!!")