n = int(input('DIGITE UM NUMERO PARA VER O FATORIAL: '))
c = n
f = 1

print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *=c
    c -= 1
print(f'{f}')