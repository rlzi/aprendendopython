cidade = str(input("Sua cidade tem santo?: ")).strip().upper()
if cidade[:5] == "SANTO":
    print("SUA CIDADE TEM SANTO")
elif cidade[5::] == "SANTO":
    print("SUA CIDADE TEM SANTO")
else:
    print("SUA CIDADE NAO TEM SANTO ")