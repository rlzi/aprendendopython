somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print(f'============- {p} PESSOA -============')
    nome = str(input(f'NOME DA {p} PESSOA: ')).strip().upper()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: [M/F]: ')).strip().upper()[0]
    somaidade += idade
    
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 +=1

mediaidade = somaidade / 4
print(f'A SOMA DA IDADE DO GRUPO E DE {mediaidade} ANOS')
print(f'O HOMEM MAIS VELHO TEM {maioridadehomem} E SEU NOME E {nomevelho}')
print(f'AO TODO SAO {totmulher20} MULHERES COM MENOS DE 20 ANOS')