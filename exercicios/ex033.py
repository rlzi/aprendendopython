n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n1 > n2 and n1 > n3:
    print(f"O MAIOR VALOR SERA {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O MAIOR VALOR SERA {n2}")
elif n3 > n1 and n3 > n2:
    print(f"O MAIOR VALOR SERA {n3}")
else:
    print("TODOS REPRESENTAM O MESMO VALOR")
    
# verifica o valor menor
if n1 < n2 and n1 < n3:
    print(f"O MENOR VALOR SERA {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O MENOR VALOR SERA {n2}")
elif n3 < n1 and n3 < n2:
    print(f"O MENOR VALOR SERA {n3}")