while True:
    sexo = str(input('QUAL SEU SEXO?: [M/F]: ')).strip().upper()[0]
    if sexo in 'Mm':
        print('SEU SEXO E MASCULINO')
        break
    elif sexo in 'Ff':
        print('SEU SEXO E FEMININO')
        break

    else:
        print('RESPOSTA INVALIDA, RESPONDA NOVAMENTE')

print('FIM DO PROGRAMA')