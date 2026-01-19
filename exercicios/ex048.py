soma = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        soma = soma + c
    
print(f'A soma de todos valores solicitados sao {soma}') # here we have the sum of all the values