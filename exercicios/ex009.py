from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.GREEN + "=" * 23)
print(Fore.GREEN + "|                     |")
print(Fore.GREEN + "| BEM VINDO A TABUADA |")
print(Fore.GREEN +"|                     |")
print(Fore.GREEN + "=" * 23)

numero = int(input("DIGITE UM NUMERO PARA VER A TABUADA: "))
print("=" * 20)
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 1, numero * 1))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 2, numero * 2))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 3, numero * 3))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 4, numero * 4))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 5, numero * 5))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 6, numero * 6))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 7 , numero * 7))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 8, numero * 8))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 9, numero * 9))
print("\033[92m{}\033[0m x \033[92m{}\033[0m = \033[91m{}\033[0m".format(numero, 10, numero * 10))
print("=" * 20)

