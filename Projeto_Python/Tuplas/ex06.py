# Crie um programa que tennha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON",
            "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR",
            "MERCADO", "PROGRAMADOR", "FUTURO")
for p in palavras:
    print(f"\nNa palavra {p} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")