from colorama import Fore, Back, Style
import time
import sys
print("\033[92m=" * 60)
print("\033[92mBEM VINDO AO PROGRAMA DE ALISTAMENTO DO EXERCITO BRASILEIRO")
print("\033[92m=\033[0m" * 60)

try:
    idade = int(input("DIGITE SUA IDADE: "))
except ValueError:
    print("\033[91mDIGITE APENAS NUMEROS!\033[0m")
    exit()


if idade == 18:
    print("\033[93m=" * 58)
    print("CARREGANDO", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(1)
    print()
    print("VOCE JA TEM IDADE PARA SE ALISTAR AO EXERCITO BRASILEIRO!")
    print("\033[93m=\033[0m" * 58)
elif idade > 18:
    while True:
        print("\rCARREGANDO", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print()
        ja_alistou = str(input("MAS VOCE JA ESTA ALISTADO?: ")).strip().upper()[0]
        if ja_alistou == "S":
            print("\033[97m=" * 30)
            print("\033[92mTUDO NOS CONFORMES, PARABENS\033[0m")
            print("\033[97m=\033[0m" * 30)
            break
        else:
            print("\033[94m=" * 45)
            print("VOCE AINDA NAO SE ALISTOU? PAGARA MULTAS")
            print("\033[94m=\033[0m" * 45)
            break
else:
    if idade < 18:
        print("\033[95m=" * 40)
        print("""AINDA NAO PODERA SE ALISTAR AO EXERCITO
EM BREVE VOCE PODERA SE ALISTAR
CONSULTE NOSSO SITE EM: https://exercitobrasileiro.gov.br""")
        anos_faltantes = 18 - idade
        print(f"FALTA {anos_faltantes} ANO(s) PARA VOCE SE ALISTAR")
