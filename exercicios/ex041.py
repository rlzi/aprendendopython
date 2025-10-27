from colorama import Style, Fore, init

init(autoreset=True)


print("\033[91m=" * 50)
print("\033[91mBEM VINDO A CONFEDERACAO ESPORTES ESCOLARES")
print("\033[91m=\033[0m" * 50)

idade_atleta = int(input("DIGITE SUA IDADE: ")) #idade do atleta

# CATEGORIAS

if idade_atleta <= 9:
    print(Fore.GREEN +"=" * 15)
    print(Fore.GREEN +"|   CATEGORIA  |") # atleta mirim
    print(Fore.GREEN +"| ATLETA MIRIM |")
    print(Fore.GREEN +"=" * 15)
    
elif idade_atleta <= 14:
    print(Fore.GREEN +"=" * 18)
    print(Fore.GREEN +"|    CATEGORIA    |")
    print(Fore.GREEN +"| ATLETA INFANTIL | ") # atleta infantil
    print(Fore.GREEN +"=" * 18)
elif idade_atleta <= 19:
    print(Fore.GREEN +"=" * 17)
    print(Fore.GREEN +"|   CATEGORIA   |")
    print(Fore.GREEN +"| ATLETA JUNIOR |") # atleta junior
    print(Fore.GREEN +"=" * 17)
elif idade_atleta <= 20:
    print(Fore.GREEN +"=" * 17)
    print(Fore.GREEN +"|   CATEGORIA   |")
    print(Fore.GREEN +"| ATLETA SENIOR |")  # atleta senior
    print(Fore.GREEN +"=" * 17)
elif idade_atleta > 20:
    print("ATLETA MASTER")  # atleta master