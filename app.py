import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from viwer.form import BotForm
from viwer.tabela import BotLog
from collections import deque
from viwer.controler import Controler



root = ttk.Window(title="Bynary BOT", themename="darkly")

bot_list = deque()
# Frame 1 Formulário
frame_form = ttk.LabelFrame(root,relief="groove",text="Formulário de Registro de Bots")
frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
form = BotForm(frame_form,bot_list)

# Frame 2 Controlador
frame_controler = ttk.LabelFrame(root,relief="groove",text="Painel de Controle")
frame_controler.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
controle = Controler(bot_list,frame_controler)



# Frame 3 Log de operações 
frame_table = ttk.LabelFrame(root,relief="groove",text="Log de Operações")
frame_table.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
log_table = BotLog(frame_table)

# Permite expansão
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()