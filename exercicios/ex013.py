salario = float(input("Qual e o Salariodo FUncionario? R$"))
novo = salario + (salario * 15 / 100)
print(f"O funcionario que Ganhava R${salario}, com 15% de aumento, passa a receber R${novo:.2f}")