from time import sleep

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
print('=' * 50)
print('                      PAINEL')
print('=' * 50)
opcao = 0
while opcao != 5:

    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR
    [ 6 ] PORCENTAGEM
    [ 7 ] DIVISAO''')

    opcao = int(input('Qual a Sua Opcao?: '))
    print('CARREGANDO...')
    sleep(1)
    if opcao == 1:
        soma = n1 + n2
        print('=' * 50)
        print(f'A SOMA ENTRE {n1} E {n2} SERA {soma}')
        print('=' * 50)
    elif opcao == 2:
        produto = n1 * n2
        print('=' * 50)
        print(f'O RESULTADO ENTRE {n1} x {n2} SERA {produto}')
        print('=' * 50)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('=' * 50)
        print(f'ENTRE {n1} E {n2} O MAIOR VALOR E {maior}')
        print('=' * 50)
    elif opcao == 4:
        print('=' * 50)
        print('Informe os Valores Novamente:')
        print('=' * 50)
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
        print('=' * 50)
    elif opcao == 5:
        print('=' * 50)
        print('FINALIZANDO...')
        sleep(1)
        print('=' * 50)
        break
    elif opcao == 6:
        porcentagem = n1 % n2
        print('=' * 50)
        print(f'A PORCENTAGEM ENTRE {n1}%{n2} sera {porcentagem}')
        print('=' * 50)
    elif opcao == 7:
        divisao = n1 / n2
        print('=' * 50)
        print(f'A DIVISAO ENTRE {n1}/{n2} SERA {divisao}')
        print('=' * 50)
    else:
        print('=' * 50)
        print('Opcao Invalida, Tente Novamente.')
        print('=' * 50)