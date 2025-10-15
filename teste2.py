import tkinter as tk

class Formulario:
    def __init__(self, lista_compartilhada, master):
        self.lista = lista_compartilhada
        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.frame)
        self.entry.pack(side="left")

        self.btn_add = tk.Button(self.frame, text="Adicionar", command=self.adicionar)
        self.btn_add.pack(side="left")

    def adicionar(self):
        valor = self.entry.get()
        if valor:
            self.lista.append(valor)  # adiciona à lista compartilhada
            self.entry.delete(0, tk.END)


class Monitor:
    def __init__(self, lista_compartilhada, master):
        self.lista = lista_compartilhada
        self.listbox = tk.Listbox(master)
        self.listbox.pack(padx=10, pady=10)
        self.monitor_loop()

    def monitor_loop(self):
        # Atualiza Listbox com novos itens
        while len(self.listbox.get(0, tk.END)) < len(self.lista):
            item = self.lista[len(self.listbox.get(0, tk.END))]
            self.listbox.insert(tk.END, item)
        # repete a cada 500ms
        self.listbox.after(500, self.monitor_loop)


# GUI principal
root = tk.Tk()
root.title("Formulario + Monitor")

lista_compartilhada = []

form = Formulario(lista_compartilhada, root)
monitor = Monitor(lista_compartilhada, root)

root.mainloop()
