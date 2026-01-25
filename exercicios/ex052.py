numero = int(input("Digite um Numero: "))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print("=" * 50)
        print("\033[33m")
        print("=" * 50)
        total = 0
    else:
        print(f"{c}", end=" ")
        print("\033[92m")
        print("=" * 50)
        print(f"O numero {numero} foi divisivel {total} vezes")
        print("=" * 50)
    total += 1
if total == 2:
    print("*" * 50)
    print("POR ISSO ELE E PRIMO")
    print("*" * 50)
else:
    print("POR ISSO ELES NAO SAO PRIMOS")