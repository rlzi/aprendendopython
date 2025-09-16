num = int(input("Informe um Numero: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 %  10
m = num // 1000 % 10
print("=" * 20)
print(f"Analisando o numero {num}")
print(f"A unidade sera {u}")
print(f"A dezena sera {d}")
print(f"A centena sera {c}")
print(f"O milhar sera {m}")