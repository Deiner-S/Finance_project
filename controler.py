import tkinter  as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
class Controler:
    def __init__(self,bot_list,master):
        self.bot_list = bot_list
        self.master = master
        self.list_box = tk.Listbox(master)
        self.list_box.grid(padx=10, pady=10)
        self.exec_list = dict()
        self.monitor()
        self.viwer_listbox()
        master.columnconfigure(0, weight=1)
        ttk.Button(master, text="Start all", command=self.start_all, width=15).grid(row=1, column=0, padx=5, columnspan=2, pady=5, sticky="w")
        ttk.Button(master, text="Stop all", command=self.stop_all, width=15).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    def viwer_listbox(self):
        self.list_box.delete(0,tk.END)
        for item in self.exec_list:
            self.list_box.insert(tk.END, item)
        self.list_box.after(500, self.viwer_listbox)

    def monitor(self):
        if self.bot_list:
            bot = self.bot_list.popleft()
            self.exec_list[bot.name] = bot
        self.master.after(300, self.monitor)

    def start_all(self):
        for bot_name in self.exec_list:
            bot = self.exec_list.get(bot_name)
            bot.start()

    def start(self,bot_name):
        bot = self.exec_list.get(bot_name)
        bot.start()

    def stop_all(self):
        for bot_name in self.exec_list:
            bot = self.exec_list.get(bot_name)
            bot.stop()

    def stop(self,bot_name):
        bot = self.exec_list.get(bot_name)
        bot.stop()

    def restart_all(self):
        for bot_name in self.exec_list:
            bot = self.exec_list.get(bot_name)
            bot.stop()
            bot.start()

    def restart(self,bot_name):
        bot = self.exec_list.get(bot_name)
        bot.stop()
        bot.start()
    
    def delete(self,bot_name):
        self.exec_list.pop(bot_name)