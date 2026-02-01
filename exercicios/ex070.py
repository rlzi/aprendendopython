from colorama import Fore, init

somatotal = maiorpreco = menorpreco = cont = 0
barato = 0
while True:
    nome = str(input("Nome Do Produto: "))
    preco = int(input("Preco: R$"))
    lista = [nome, preco]
    if preco >= 1000:
        maiorpreco +=1
    elif preco <=1000:
        menorpreco +=1
    if cont ==1:
        menorpreco = preco
        barato = preco
    else:
        if preco < menorpreco:
            menorpreco = preco
    somatotal += preco
    continuar = str(input("Quer Continuar? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Quer Continuar? "))
    if continuar in "N":
        break
    elif continuar in  "S":
        continue
print(Fore.BLUE +"=========INFORMACAO DA COMPRA==========")
print(f"O Total da compra foi R${somatotal}.00")
print(f"Temos 1 Produtos custando mais de R$1000.00")
print(f"O Produto Mais barato foi {barato} que custa R${menorpreco}")