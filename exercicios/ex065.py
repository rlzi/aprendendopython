resp = "S"
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    
    resp = str(input('Quer Continuar?: [S/N]')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} e a media foi {media}')
print('Fim Do Programa')