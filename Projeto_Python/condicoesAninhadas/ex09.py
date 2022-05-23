# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando seu preço normal e condição de pagamento:
# - A vista dinheiro/cheque: 10% de desconto
# -A vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal 
# -3x ou mais no cartão: 20% de juros

print("{:=^40}".format("LOJAS M&M's"))
preco = float(input("Preço das compras: R$ "))
print("""Formas de pagamento
        [1] á vista dinheiro/cartão
        [2] á vista cartão
        [3] 2x no cartão
        [4] 3x ou mais no cartão""")
opcao = int(input("Qual é a opção? "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
     total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcela = int(input("Quantas parcelas? "))
    parcela = total / totalParcela
    print("Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS".format(totalParcela, parcela))
else:
    total = preco
    print("Opção inválida de pagamento. Tente novamente! ")

print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.".format(preco, total))