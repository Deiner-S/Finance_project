import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Janela com tema
app = ttk.Window(title="Exemplo LabelFrame", themename="darkly")

# LabelFrame (Frame com título)
frame = ttk.LabelFrame(app, text="Painel de Bot", padding=10, bootstyle="info")
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Conteúdo dentro do LabelFrame
label = ttk.Label(frame, text="Este é o conteúdo do frame")
label.pack(pady=5)

botao = ttk.Button(frame, text="Clique aqui", bootstyle="success")
botao.pack(pady=5)

app.mainloop()
