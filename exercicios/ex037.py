n = int(input("Digite um numero inteiro: "))
print("""ESCOLHA UMA DAS BASES PARA CONVERTER
---------------------------------
[1] CONVERTER PARA BINARIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL
---------------------------------""")
opcao = int(input("SUA OPCAO: "))
if opcao == 1:
    print(f"{n} CONVERTIDO PARA BINARIO E IGUAL A {bin(n)[2:]}")
elif opcao == 2:
    print(f"{n} CONVERTIDO PARA OCTAL E IGUAL A {oct(n)[2:]}")
elif opcao == 3:
    print(f"{n} CONVERTIDO PARA HEXADECIMAL E IGUAL A {hex(n)[2:]}")