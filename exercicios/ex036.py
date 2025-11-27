print("=" * 40)
print("BANCO MG - SOLICITAR EMPRESTIMO BANCÁRIO") #Título
print("=" * 40)

valor_casa = float(input("qual o valor da casa que deseja comprar? R$"))
salario_comprador = float(input("qual o salario do comprador? R$"))
anos_pra_pagar = int(input("em quantos anos deseja pagar? "))

if salario_comprador * 0.3 >= (valor_casa / (anos_pra_pagar * salario_comprador)):
    print("\033[32mEMPRESTIMO CONCEDIDO!\033[0m")
    print(f"para pagar uma casa no valor de R${valor_casa:.2f} em {anos_pra_pagar} anos")
    print(f"a prestacao mensal sera de R${(valor_casa / anos_pra_pagar * 12)}")
    
else:
    print("\033[31mEMPRESTIMO NEGADO!\033[m")