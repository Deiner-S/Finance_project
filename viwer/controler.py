import tkinter  as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

class Controler:
    def __init__(self,bot_list,frame):
        self.bot_list = bot_list
        self.frame = frame
        self.exec_list = dict()
        self.tree = self.generate_table()
        self.monitor()
        #master.columnconfigure(0, weight=1)
        ttk.Button(frame, text="Start", command=self.start, width=10).grid(row=1, column=0, padx=5, columnspan=2, pady=5, sticky="w")
        ttk.Button(frame, text="Stop", command=self.stop, width=10).grid(row=1, column=0, padx=5, pady=5, sticky="e")
    
    def generate_table(self):
        # --- Frame para a tabela ---
        self.frame = ttk.Frame(self.frame, relief="groove")
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        # --- Criando a tabela ---
        columns = ("name", "status")
        tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        # Definindo os títulos das colunas
        tree.heading("name", text="Strategy")
        tree.heading("status", text="Status")

        # Definindo largura das colunas
        tree.column("name", width=100)
        tree.column("status", width=100)       

        tree.grid(row=0, column=0)
        return tree

    def monitor(self):
        if self.bot_list:
            bot = self.bot_list.popleft()
            self.exec_list[bot.name] = bot
            self.tree.insert("", "end", values=(bot.name, "on hold"))            
        self.frame.after(300, self.monitor)

    def stop(self):
        selecionados = self.tree.selection()
        if selecionados:
            for item_id in selecionados:                
                valores = self.tree.item(item_id, "values")
                if valores[1] == "on hold":
                    messagebox.showwarning("Aviso", f"Bot {valores[0]} still on hold")
                else: 
                    bot = self.exec_list.get(valores[0])
                    bot.stop()
                    self.exec_list.pop(valores[0])
                    self.tree.delete(item_id)
        else:
            messagebox.showwarning("Aviso", "No bots were selected")

    def start(self):
        selecionados = self.tree.selection()
        if selecionados:
            for item_id in selecionados:
                
                valores = self.tree.item(item_id, "values")
                if valores[1] == "Running":
                    messagebox.showwarning("Aviso", f"Bot {valores[0]} has already started")
                else: 
                    bot = self.exec_list.get(valores[0])
                    self.tree.item(item_id, values=[valores[0],"Running"])
                    bot.start()
        else:
            messagebox.showwarning("Aviso", "No bots were selected")
    