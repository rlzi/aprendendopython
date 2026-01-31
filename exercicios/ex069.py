maior = homem = mulher20 = 0
while True:
    print("=" * 40)
    print("CADASTRE UMA PESSOA")
    print("=" * 40)
    print("-" *40)
    idade = int(input("Idade: "))
    print("-" * 40)
    if idade > 18:
        maior +=1
    print("-" * 40)
    sexo = str(input("Sexo: [M/F]: ")).strip().upper()[0]
    print("-" * 40)
    if sexo in "M":
        homem +=1
    else:
        if idade <20 and sexo in "F":
            mulher20 +=1
    print("-+" * 40)
    continuar = str(input("Quer Continuar? [S/N]: ")).strip().upper()[0]
    print("-+" * 40)
    if continuar in "S":
        continue
    else:
        break

print("=======================PAINEL=========================")

print(f"Total De pessoas com mais de 18 anos: {maior}")
print(f"Ao todo, temos {homem} homens cadastrados")
print(f"E temos {mulher20} mulheres com menos de 20 anos")