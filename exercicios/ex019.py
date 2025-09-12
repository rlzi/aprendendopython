from random import choice
#Entrada de usuarios
aluno1 = str(input("Digite O Primeiro Aluno: "))
aluno2 = str(input("Digite O Segundo Aluno: "))
aluno3 = str(input("Digite O Terceiro Aluno: "))
aluno4 = str(input("Digite O Quarto Aluno: "))


lista = [aluno1, aluno2, aluno3, aluno4] #Lista de alunos
escolhido = choice(lista) #Ramdomiza e escolhe um da Lista
print(f"O Escolhido Foi {escolhido}") #Mostra Na tela o ESCOLHIDO