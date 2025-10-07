import tkinter as tk
from form import BotForm
from tabela import bot_log
import threading
root = tk.Tk()

# Frame 1
frame_form = tk.Frame(root, bd=2, relief="groove")
frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
form = BotForm(frame_form)

# Frame 2 (se quiser outro formulário)
frame_table = tk.Frame(root, bd=2, relief="groove")
frame_table.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
table = bot_log(frame_table)
monitor_table_thread = threading.Thread(target=table.add_bot_log)
monitor_table_thread.start()
# Permite expansão
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()