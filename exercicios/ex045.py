import random
import time

print("================================================")
print("==============COMPUTADOR JOKEN PO!==============")
print("================================================")

print("""Suas Opcoes:
            [0] PEDRA
            [1] PAPEL
            [2] TESOURA""")

jogador = int(input("Digite Sua Escolha: "))

computador = 0 

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!")

print("================================================")
#Painel Jogador

if jogador == 0:
    print("VOCE JOGOU PEDRA")
elif jogador == 1:
    print("VOCE JOGOU PAPEL")
elif jogador == 2:
    print("VOCE JOGOU TESOURA")

print("================================================")
#Painel Computador 

if computador == 0:
    print("COMPUTADOR JOGOU PEDRA")
elif computador == 1:
    print("COMPUTADOR JOGOU PAPEL") 
elif computador == 2:
    print("COMPUTADOR JOGOU TESOURA")   

print("================================================")

if jogador > computador:
    print("JOGADOR VENCEU")
elif computador > jogador:
    print("EU GANHEI")
elif jogador == computador:
    print("JOGO EMPATADO!")