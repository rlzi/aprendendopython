numero = int(input('Digite um numero [999 PARA PARAR]: '))
total = numero
vezes = 0
while True:
    print('=' * 40)
    numero = int(input('Digite um numero [999 PARA PARAR]: '))
    vezes +=1
    total += numero
    if numero == 999:
        break
print(f'Voce digitou {vezes} numeros e a soma entre eles foi {total -999}')
print('Fim do Programa')