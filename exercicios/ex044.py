import tkinter as tk
from colorama import Fore, Style, Init
from tkinter import messagebox
root = tk.Tk()
root.title("first")
root.geometry("400x500")
label = tk.Label(root, text="OLA MUNDO")
label.pack()
botao = tk.Button(root, text="clique aqui", command=True)
botao.pack(pady=10)
root.mainloop()