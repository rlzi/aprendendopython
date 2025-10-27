print("\033[92m=" * 60)
print("\033[92mBEM VINDO AO PROGRAMA DE ALISTAMENTO DO EXERCITO BRASILEIRO")
print("\033[92m=\033[0m" * 60)
idade = int(input("DIGITE SUA IDADE: "))
if idade == 18:
    print("\033[93m=" * 58)
    print("VOCE JA TEM IDADE PARA SE ALISTAR AO EXERCITO BRASILEIRO!")
    print("\033[93m=\033[0m" * 58)
elif idade > 18:
    mas_cadastrou = str(input("MAS VOCE JA ESTA ALISTADO?: ")).strip().upper()[0]
    if mas_cadastrou == "S":
        print("\033[97m=" * 30)
        print("\033[92mTUDO NOS CONFORMES, PARABENS\033[0m")
        print("\033[97m=\033[0m" * 30)
    else:
        print("\033[94m=" * 45)
        print("VOCE AINDA NAO SE ALISTOU? PAGARA MULTAS")
        print("\033[94m=\033[0m" * 45)
else:
    if idade < 18:
        print("\033[95m=" * 40)
        print("""AINDA NAO PODERA SE ALISTAR AO EXERCITO
EM BREVE VOCE PODERA SE ALISTAR
CONSULTE NOSSO SITE EM: https://exercitobrasileiro.gov.br""")
