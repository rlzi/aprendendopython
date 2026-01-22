numero = int(input("Digite um Numero: "))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print("\033[33m")
        total +=1
    else:
        print(f"{c}", end=" ")
        print("\033[92m")
print(f"O numero {numero} foi divisivel {total} vezes")