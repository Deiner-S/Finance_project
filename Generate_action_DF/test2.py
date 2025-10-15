import tkinter as tk
from tkinter import messagebox
from threading import Thread
from src.quark_strategy import QuarkStrategy

class BotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Bots")
        self.bots = []

        # Labels e Entrys
        tk.Label(master, text="Email:").grid(row=0, column=0)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=0, column=1)

        tk.Label(master, text="Senha:").grid(row=1, column=0)
        self.senha_entry = tk.Entry(master, show="*")
        self.senha_entry.grid(row=1, column=1)

        tk.Label(master, text="Valor por operação:").grid(row=2, column=0)
        self.valor_entry = tk.Entry(master)
        self.valor_entry.grid(row=2, column=1)

        tk.Label(master, text="Ativo:").grid(row=3, column=0)
        self.ativo_entry = tk.Entry(master)
        self.ativo_entry.grid(row=3, column=1)

        tk.Label(master, text="Limite Martingale:").grid(row=4, column=0)
        self.martingale_entry = tk.Entry(master)
        self.martingale_entry.grid(row=4, column=1)

        tk.Label(master, text="Tipo de Conta:").grid(row=5, column=0)
        self.tipo_entry = tk.Entry(master)
        self.tipo_entry.grid(row=5, column=1)

        # Botões
        tk.Button(master, text="Adicionar Bot", command=self.add_bot).grid(row=6, column=0, pady=10)
        tk.Button(master, text="Iniciar Bots", command=self.start_bots).grid(row=6, column=1, pady=10)

    def add_bot(self):
        try:
            email = self.email_entry.get()
            senha = self.senha_entry.get()
            valor = int(self.valor_entry.get())
            ativo = self.ativo_entry.get()
            martingale = int(self.martingale_entry.get())
            tipo = self.tipo_entry.get().upper()

            quark = QuarkStrategy(email, senha, valor, ativo, martingale, tipo)
            bot_thread = Thread(target=quark.strategy_runner)
            self.bots.append(bot_thread)

            messagebox.showinfo("Sucesso", f"Bot adicionado! Total de bots: {len(self.bots)}")
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao adicionar bot:\n{e}")

    def start_bots(self):
        if not self.bots:
            messagebox.showwarning("Atenção", "Nenhum bot adicionado!")
            return

        for bot in self.bots:
            bot.start()
        messagebox.showinfo("Info", "Todos os bots foram iniciados!")

    def clear_entries(self):
        self.email_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)
        self.valor_entry.delete(0, tk.END)
        self.ativo_entry.delete(0, tk.END)
        self.martingale_entry.delete(0, tk.END)
        self.tipo_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = BotApp(root)
    root.mainloop()
