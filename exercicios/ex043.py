preco = float(input("PRECO DO PRODUTO: R$"))
print("=" * 30)
print("""
============================================
            FORMAS DE PAGAMENTO
    
[1] DINHEIRO/CHEQUE | 10% DESCONTO
[2] A VISTA NO CARTAO | 5% DESCONTO
[3] EM ATE 2x NO CARTAO | PRECO NORMAL
[4] 3x OU MAIS NO CARTAO | 20% JUROS
=============================================
""")

escolha = int(input("DIGITE SUA FORMA DE PAGAMENTO: "))
if escolha == 1:
    novo = 0
    desconto = novo - (preco - 10 / 100)
    novo +=1
    print(desconto)
    