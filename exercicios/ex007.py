n1 = float(input("Digite A Primeira Nota: "))
n2 = float(input("Digite A Segunda Nota: "))
media = (n1 + n2) / 2
print(f"A MEDIA ENTRE {n1} E {n2} SERA {media:.2f}")
if media >= 5:
    print(f"PARABENS,VOCE FOI \033[92mAPROVADO\033[0m")
else:
    print("\033[91mREPROVADO!\033[0m ESTUDE MAIS!!!")