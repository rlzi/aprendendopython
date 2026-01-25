import random
tentativas = 55
print('=' * 50)
print('SOU SEU COMPUTADOR...')
print('ACABEI DE PENSAR EM UM NUMERO ENTRE 0 E 10.')
print('SERA QUE VOCE CONSEGUE ADIVINHAR QUAL FOI?')
print('=' * 50)
jogador = int(input('QUAL E SEU PALPITE?: '))
print('=' * 50)
computador = random.randint(0,10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('QUAL E SEU PALPITE?: '))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS...')
        elif jogador > computador:
            print('MENOS...')
            
print(f'ACERTOU COM {palpites} PALPITES, PARABENS!')