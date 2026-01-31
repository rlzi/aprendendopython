numero = int(input("Digite Um numero Para Ver a Tabuada: "))
while True:
    print("=" * 40)
    for c in range(1,11):
        print(f"{numero} x {c} = {numero*c}")
    print("=" * 40)
    numero = int(input("Quer ver a tabuada de qual valor?: "))
    if numero <0:
        break
print("PROGRAMA DE TABUADA ENCERRADO!!!, volte sempre!")