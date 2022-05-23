#Criei um mini sistema de cadastro de animais com a finalidade de treinar as funcionalidades utilizando dicionários.

from time import sleep
db = []

print("-=-=-=-=-CADASTRO DE ANIMAL-=-=-=-=-")
nome = str(input("Nome do animal: "))
especie = str(input("Espécie do animal: "))
cor = str(input("Cor do animal: "))
print("-=" * 30)

animal = {
    'name': nome,
    'species': especie,
    'color': cor
}

animal['name'] = nome
animal['species'] = especie
animal['color'] = cor

db.append(animal)
print(db)

opcao = 0

while opcao != 5:
    print("-=" * 30)
    print("""
O que você quer fazer?\n
[1] - Listar animais
[2] - Cadastrar novo animal
[3] - Remover um cadastro do sistema
[4] - Atualizar um cadastro 
[5] - Sair
""")
    opcao = int(input("Opção: "))
    if opcao == 1:
        print("-=-=-=-=-LISTA DE ANIMAIS-=-=-=-=-")
        for keey, valuee in animal.items():
            print(f"{keey} = {valuee}")

    elif opcao == 2:
        print("---Novo cadastro de animal---")
        nome = str(input("nome do animal: "))
        especie = str(input("especie do animal: "))
        cor = str(input("Cor do animal: "))
        print("Carregando...")
        sleep(1)
        print("-=" * 30)
        print("Novo cadastro realizado com sucesso!")
        db.append(animal)

    elif opcao == 3:
        db.remove(animal)
        print("REMOVENDO CADASTRO, AGUARDE...")
        sleep(1)
        print("Cadastro removido com sucesso!")

    elif opcao == 4:
            resposta = int(input("""Qual dado você deseja atualizar? Escolha a opção a seguir: 
            [1] - Nome
            [2] - Espécie
            [3] - Cor\n"""))
            if resposta == 1:
                print("Digite o nome que deseja para atualizar cadastro: ")
                animal.update({'name': input()})
            elif resposta == 2:
                print("Digite a espécie que deseja para atualizar cadastro: ")
                animal.update({'species': input()})
            elif resposta == 3:
                print("Digite a cor que deseja para atualizar cadastro: ")
                animal.update({'color': input()})
    elif opcao == 5:
        print("SAINDO...")
        sleep(1)
        print("Você saiu do sistema, volte sempre!!!")
        break
    else:
        print("COMANDO INVÁLIDO! Tente novamente. ")
print("-=" * 30)
print(db)