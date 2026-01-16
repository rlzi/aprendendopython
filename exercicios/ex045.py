from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas Opcoes:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')

jogador = int(input('qual e a sua jogada? '))
print('=' * 12)
print(f'Computador Jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

if computador == 0: #computador joga pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    
    else:
        print("JOGADA INVALIDA")

elif computador == 1: #computador joga papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA")

elif computador == 2: #computador joga tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("ENTRADA INVALIDA")