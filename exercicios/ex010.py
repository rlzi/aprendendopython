real = float(input("\033[94mQUANTOS REAIS VOCE TEM NA CARTEIRA? R$\033[0m"))
dolar = real / 5.39
print(f"COM \033[92mR${real}\033[0m VOCE PODE COMPRAR \033[91mUS${dolar:.0f}\033[0m")