distancia = float(input("Qual a distancia da sua viagem?: "))
print(f"voce esta prestes a iniciar uma viagem de {distancia:.2f}km")
if distancia <200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"E o Preco da sua passagem da viagem sera de R${preco}")