import tkinter as tk
import random
from tkinter import messagebox

# Criar a janela principal
janela = tk.Tk()
janela.title("Meu Primeiro Programa")
janela.geometry("400x300")

def usuario():
    nome = entrada_nome.get()
    lista_nomes = ["julia", "maria", "joaquim"]
    if lista_nomes == nome:
        nome.random(lista_nomes)
    if nome:
        messagebox.showinfo("Meu Primeiro Software", f"BEM VINDO {lista_nomes}")
    else:
        messagebox.showwarning("ERRO", "INSIRA SEUS DADOS CORRETAMENTE")
    
rotulo = tk.Label(janela, text="DIGITE SEU NOME:", font=("Arial", 12))
rotulo.pack(pady=10)

entrada_nome = tk.Entry(janela, font=("Arial", 15))
entrada_nome.pack(pady=5)
lista_nomes = tk.Label(janela, background="black", font=("Arial", 12))
lista_nomes.pack(pady=10)
botao = tk.Button(janela, text="Clique Aqui", command=usuario, bg="green", font=("SansSerif", 12))
botao.pack(pady=10)
janela.mainloop()
