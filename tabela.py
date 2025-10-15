import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
class BotLog():
    def __init__(self,frame):
        self.frame = frame
        self.tree = self.generate_table()
    def generate_table(self):
        # --- Frame para a tabela ---
        self.frame = ttk.Frame(self.frame, relief="groove")
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        # --- Criando a tabela ---
        columns = ("email", "valor", "ativo", "martingale", "tipo")
        tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        tree.heading("email", text="Email")
        tree.heading("valor", text="Valor por operação")
        tree.heading("ativo", text="Ativo")
        tree.heading("martingale", text="Limite Martingale")
        tree.heading("tipo", text="Tipo de Conta")

        # Definindo largura das colunas
        tree.column("email", width=150)
        tree.column("valor", width=120)
        tree.column("ativo", width=100)
        tree.column("martingale", width=120)
        tree.column("tipo", width=120)

        tree.pack(fill="both", expand=True)
        return tree

    # --- Função para adicionar dados à tabela ---
    def add_bot_log(self):
        print("start thread")
        while True:
            with open("log.txt", "r") as f:
                linhas = f.readlines()  # lê todas as linhas
                ultima = linhas[-1].strip()
                data = ultima.split(",")
            self.tree.insert("", "end", values=(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            ))
            time.sleep(15)

    
