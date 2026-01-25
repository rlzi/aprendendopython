frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A FRASE E UM PALINDROMO')
else:
    print("A FRASE DIGITADA NAO E UM PALINDROMO")