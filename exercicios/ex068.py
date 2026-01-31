from random import randint
v = 0
while True:
    jogador = int(input("Diga Um Valor: "))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("PAR OU IMPAR?: ")).strip().upper()[0]
    print(f"Voce jogou {jogador} e o computador jogou {computador}. Total de {total}")
    if tipo == "P":
        if total % 2 == 0:
            print("Voce Venceu!")
            v +=1
        else:
            print("Voce Perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Voce Venceu!")
            v +=1

        else:
            print("Voce Perdeu!")
            break
    print("Vamos Jogar Novamente...")
print(f"Fim de Jogo. Voce venceu {v} vezes.")