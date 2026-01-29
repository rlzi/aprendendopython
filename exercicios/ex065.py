resp = "S"
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer Continuar?: [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} e a media foi {media}')
print(f'O maior numero foi {maior} o menor numero foi {menor}')
print('Fim Do Programa')