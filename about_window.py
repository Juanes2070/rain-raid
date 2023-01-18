import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)

        text_str = 'Programa desarrollado por Juanes Marín. \n\n ' \
                   'Los valores de calibración por defecto para\n' \
                   'la relación ZR fueron tomados del SIATA.\n\n ' \
                   'Universidad de Medellín  2023. \n '

        self.about_label = ttk.Label(self.window)
        self.about_label.configure(text=text_str)
        self.about_label.grid(row=0, column=0)

        self.close_button = ttk.Button(self.window)
        self.close_button.configure(text='Salir', command=self.window.destroy)
        self.close_button.grid(row=1,column=0,sticky='ew')
