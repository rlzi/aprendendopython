import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
janela = tk.Tk()
janela.title("Meu Primeiro Programa")
janela.geometry("400x300")

def clicou_botao():
    nome = entrada_nome.get()
    if nome:
        messagebox.showinfo("Mensagem" f"ola, {nome}! Bem Vindo")
    else:
        messagebox.showwarning("Aviso.", f"Por Favor, Digite Seu nome.")
    
rotulo = tk.Label(janela, text="Digite Seu Nome:", font=("Arial", 14))
rotulo.pack(pady=10)

entrada_nome = tk.Button(janela, text="Clique Aqui!", command=clicou_botao, bg="lightblue", font=("Arial", 12))
entrada_nome.pack(pady=5)

botao = tk.Button(janela, text="", font=("Arial", 10))
botao.pack(pady=10)

mensagem = tk.Label(janela, text="", font=("Arial", 10))
mensagem.pack(pady=10)

janela.mainloop()