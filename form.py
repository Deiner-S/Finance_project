import tkinter as tk
from tkinter import messagebox

class BotForm:
    def __init__(self, master):
        self.master = master
        #self.master.title("Configuração de Bots")
        self.bots = []

        # Labels e Entries
        self.create_label_entry("Email:", 0)
        self.create_label_entry("Senha:", 1, show="*")
        self.create_label_entry("Valor por operação:", 2)
        self.create_label_entry("Ativo:", 3)
        self.create_label_entry("Limite Martingale:", 4)
        self.create_label_entry("Tipo de Conta (DEMO/PRINCIPAL):", 5)

        # Botões
        tk.Button(master, text="Adicionar", command=self.add_bot, width=15).grid(row=6, column=0, padx=5, columnspan=2, pady=5, sticky="w")
        tk.Button(master, text="Limpar", command=self.clear_entries, width=15).grid(row=6, column=1, padx=5, pady=5, sticky="w")

    def create_label_entry(self, text, row, show=None):
        tk.Label(self.master, text=text).grid(row=row, column=0, padx=5, pady=0, sticky="w")
        entry = tk.Entry(self.master, show=show)
        entry.grid(row=row, column=1, padx=0, pady=5)
        setattr(self, f"entry_{row}", entry)

    def add_bot(self):
        try:
            bot_data = {
                "email": self.entry_0.get(),
                "senha": self.entry_1.get(),
                "valor": int(self.entry_2.get()),
                "ativo": self.entry_3.get(),
                "martingale": int(self.entry_4.get()),
                "tipo": self.entry_5.get().upper()
            }
            self.bots.append(bot_data)
            messagebox.showinfo("Sucesso", f"Bot adicionado! Total de bots: {len(self.bots)}")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao adicionar bot:\n{e}")

    def clear_entries(self):
        for i in range(6):
            getattr(self, f"entry_{i}").delete(0, tk.END)



