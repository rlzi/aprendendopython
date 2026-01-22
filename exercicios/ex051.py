primeiro = int(input("Primeiro Termo: "))
razao = int(input("Razao: "))
decimo = primeiro + (11 -1) * razao
for c in range(primeiro, decimo, razao):
    print(f"{c}", end=" -> ")
print("ACABOU")