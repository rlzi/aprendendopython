dias = int(input("Quantos Dias alugados? "))
km = float(input("Quantos Km rodados? "))
pago  = (dias * 60) + (km * 0.15)
print(f"O total a pagar e de R${pago}")