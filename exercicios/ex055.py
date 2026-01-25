maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'PESO DA {p} PESSOA: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = maior
        if peso < menor:
            menor = menor

print(f'O MAIOR PESO LIDO FOI DE {maior}kg')
print(f'O MENOR PESO LIDO FOI DE {menor}kg')