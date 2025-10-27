nota1 = float(input("DIGITE A PRIMEIRA NOTA: "))
nota2 = float(input("DIGITE A SEGUNDA NOTA: "))
media = (nota1 + nota2) / 2
print(f"A MEDIA SERA {media}")
if media >= 7.0:
    print("APROVADO, PARABENS")
elif media >= 5.5 or 6.9:
    print("EM RECUPERACAO") 
else:
    print("REPROVADO, ESTUDE MAIS!!!")