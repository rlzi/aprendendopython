from datetime import date
ano = int(input("DIGITE O ANO PARA ANALISAR: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print("ANO BISSEXTO")
else:
    print("ANO NAO BISSEXTO")