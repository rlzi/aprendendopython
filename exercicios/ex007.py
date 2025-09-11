n1 = float(input("Digite A Primeira Nota: "))
n2 = float(input("Digite A Segunda Nota: "))
media = (n1 + n2) / 2
print(f"A MEDIA ENTRE E{n1} e {n2} SERA {media:.2f}")
if media >= 5:
    print(f"PARABENS, APROVADO")
else:
    print("REPROVADO! ESTUDE MAIS!!!")