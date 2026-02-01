print("=" * 50)
print("BANCO BRASIL")
print("=" * 50)
valor = int(input("Digite o Valor para Saque: R$"))
total = valor
cedulas = 50
totalcedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalcedulas +=1
    else:
        if totalcedulas > 0:
            print(f"TOTAL DE {totalcedulas} CEDULAS DE R${cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalcedulas = 0
        if total == 0:
            break
print('='* 30)
print("VOLTE SEMPRE...")
print('='* 30)