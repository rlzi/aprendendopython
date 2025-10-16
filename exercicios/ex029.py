from colorama import Fore, Style, init

init(autoreset=True)

print("=" * 40)
velocidade = int(input("Bom DIa, Qual a Velocidade Atual Do Carro?: "))
print("=" * 40)
if velocidade <= 80:
    print(Fore.GREEN +"Tenha Um bom dia E dirija Com Seguranca." + Fore.RESET)

else:
    multa = (velocidade-80) * 7
    print(Fore.RED + "MULTADO!!!, Voce excedeu o limite de velocidade da Via de 80km/h")
    print(f"Voce deve Pagar Uma Multa de R${multa:.2f}" + Fore.RESET)
    print(Fore.GREEN + "Tenha Um bom dia E dirija Com Seguranca." + Fore.RESET)