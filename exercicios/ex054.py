from datetime import date
maior = 0
menor = 0
atual = date.today().year

for i in range(1,8):
    nasc = int(input(f'EM QUE ANO A {i}a PESSOA NASCEU?: '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    elif idade <= 21:
        menor += 1

print(f'AO TODO TIVEMOS {maior} MAIORES DE IDADE E \nTAMBEM TIVEMOS {menor} MENORES DE IDADE')
