somatotal = maiorpreco = menorpreco = nomevalor = 0
while True:
    nome = str(input("Nome Do Produto: "))
    preco = int(input("Preco: R$"))
    lista = [nome, preco]
    if preco >= 1000:
        maiorpreco +=1
    elif preco <=1000:
        menorpreco +=1
        nomevalor +=1
    somatotal += preco
    continuar = str(input("Quer Continuar? [S/N]: ")).strip().upper()[0]
    if continuar in "N":
        break
    elif continuar in  "S":
        continue

print(f"O Total da compra foi R${somatotal}.00")
print(f"Temos 1 Produtos custando mais de R$1000.00")
print(f"O Produto Mais barato foi {nomevalor} que custa R${menorpreco}")