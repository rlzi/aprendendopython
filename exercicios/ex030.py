import time

print("=" * 40)
print("BEM VINDO AO PROGRAMA DE IMPAR E PAR")
print("=" * 40)

n = int(input("DIGITE UM NUMERO: "))
print("CARREGANDO...")
time.sleep(3)
resultado = n % 2
if resultado == 1:
    print("impar")
else:
    print("par")
