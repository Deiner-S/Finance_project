import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from bot import Bot

class BotForm:
    def __init__(self, master,bots_list):
        self.master = master
        self.bots_list = bots_list
        master.columnconfigure(1, weight=1)
        # Labels e Entries
        
        self.create_label_entry("Email:", 0)
        self.create_label_entry("Senha:", 1, show="*")
        self.create_label_entry("Valor por operação:", 2)
        self.create_label_entry("Ativo:", 3)
        self.create_label_entry("Tipo de Conta (DEMO/PRINCIPAL):", 4)

        # Botões
        ttk.Button(master, text="Adicionar", command=self.add_bot, width=15).grid(row=6, column=3, padx=5, pady=5, sticky="w")
        ttk.Button(master, text="Limpar", command=self.clear_entries, width=15).grid(row=6, column=3, padx=5, pady=5, sticky="e")

    def create_label_entry(self, text, row, show=None):
        ttk.Label(self.master, text=text).grid(row=row, column=0, padx=5, pady=0, sticky="w")
        entry = ttk.Entry(self.master,show=show,width=50)
        entry.grid(row=row, column=3, padx=5, pady=5,sticky="e")
        setattr(self, f"entry_{row}", entry)

    def add_bot(self):
        try:
            bot = Bot(
                      email=self.entry_0.get(),
                      password=self.entry_1.get(),
                      operation_value=int(self.entry_2.get()),
                      active=self.entry_3.get(),
                      account_type= self.entry_4.get().upper()
                      )
            self.bots_list.append(bot)
            messagebox.showinfo("Sucesso", f"Bot adicionado! Total de bots: {len(self.bots_list)}")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao adicionar bot:\n{e}")

    def clear_entries(self):
        for i in range(5):
            getattr(self, f"entry_{i}").delete(0, tk.END)



