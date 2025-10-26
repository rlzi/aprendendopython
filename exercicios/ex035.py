print("=" * 20)
print("ANALISADOR DE TRIANGULOS")
print("=" * 20)
r1 = float(input("\033[34mprimeiro segmento:\033[m "))
r2 = float(input("segundo segmento: "))
r3 = float(input("terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print("os segmentos acima podem formar um triangulo")
else:
     print("os segmentos acima nao podem formar um triangulo")