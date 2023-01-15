import tkinter as tk

class Menu:
    def __init__(self, root):
        self.root = root

        self.menubar = tk.Menu(self.root,background="blue")
        self.menubar.configure()
        self.root.config(menu=self.menubar)

        self.main_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='Menu', menu=self.main_menu)
        self.main_menu.add_command(label='Manual de usuario')
        self.main_menu.add_command(label='Descripción de procesos')
        self.main_menu.add_command(label='Acerca de')
        self.main_menu.add_command(label='Salir', command=self.root.destroy)

