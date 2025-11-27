from colorama import Fore, Back, Style
print(Fore.GREEN + Style.BRIGHT + "--------------------------------------------")
print("    BEM VINDO AO CONVERSOR DE VALORES")
print("--------------------------------------------")
n = int(input("DIGITE UM NUMERO: "))
print("--------------------------------------------" + Fore.RESET)

print(Fore.BLUE + """
=================================================
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL
=================================================""" + Fore.RESET)

opcao = int(input(Fore.BLACK + "ESCOLHA A OPCAO PARA CONVERTER: "+ Fore.RESET)) #escolher para qual converter

#opcoes

if opcao == 1:
    print(f"O NUMERO {n} CONVERTIDO PARA BINARIO SERA {bin(n)}")
elif opcao == 2:
    print(f"O NUMERO {n} CONVERTIDO PARA OCTAL SERA {oct(n)}")
elif opcao == 3:
    print(f"O NUMERO {n} CONVERTIDO PARA HEXADECIMAL SERA {hex(n)}")
else:
    print("OPCAO INVALIDA")