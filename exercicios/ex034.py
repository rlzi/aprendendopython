salario = float(input("Qual o Salario do funcionario? R$"))
if salario > 1250:
    novo = salario + salario * (10 / 100)
    print(f"O FUNCIONARIO QUE RECEBIA R${salario:.2f}, com 10% de AUMENTO IRA RECEBER R${novo:.2f}")
else:
    novo = salario + salario * (15 / 100)
    print(f"O FUNCIONARIO QUE RECEBIA R${salario:.2f}, com 15% de aumento ira receber R${novo:.2f}")