cidade = str(input("Em que cidade voce nasceu: ")).strip().upper()
if cidade.startswith('SANTO',):
    print("SUA CIDADE TEM SANTO")
else:
    print("SUA CIDADE NAO TEM SANTO")

if cidade.endswith("SANTO"):
    print("SUA CIDADE TEM SANTO NO NOME")
else:
    print("SUA CIDADE NAO TEM SANTO NO NOME")