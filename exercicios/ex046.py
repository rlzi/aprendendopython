from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

print(f"o computador escolheu {itens[computador]}")