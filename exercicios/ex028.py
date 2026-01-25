import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

print("=" * 65) #shift + ins duplica assim
print(Fore.RED + "Ola, EU sou um computador E vou pensar Em um numero Entre 0 E 5. " + Fore.RESET)
print("=" * 65)
computador = random.randint(0,10)
while True:
    jogador = int(input("EM QUE NUMERO EU PENSEI?: "))
    print(Fore.GREEN + "PROCESSANDO SUA RESPOSTA..." + Fore.RESET)
    computador = 0
    time.sleep(3)
    if jogador == computador:
        print('-' * 34)
        print("voce ganhou por sorte 🤣")
        print("-" * 34)
    else:
        print("-" * 65)
        print(f"Eu ganhei KKKK, eu pensei no numero {computador} e nao no {jogador} KKKKKK SEU BOT ")
        print("-" * 65)
    print(Fore.CYAN +"=+" * 35)
    tentar_novamente = str(input("DESEJA TENTAR NOVAMENTE? S/N: ")).strip().upper()[0]
    print(Fore.CYAN + "+=" * 35 + Fore.RESET)
    if tentar_novamente != "S":
        print("ENCERRANDO O PROGRAMA...")
        break