import tkinter as tk
import res_path
import webbrowser


class Menu:
    def __init__(self, root):
        self.root = root

        self.menubar = tk.Menu(self.root,background="blue")
        self.menubar.configure()
        self.root.config(menu=self.menubar)

        self.main_menu = tk.Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label='Menu', menu=self.main_menu)
        self.main_menu.add_command(label='Manual de usuario', command= lambda: open_user_manual())
        self.main_menu.add_command(label='Descripción de procesos', command=lambda: open_process_manual())
        self.main_menu.add_command(label='Acerca de')
        self.main_menu.add_command(label='Salir', command=self.root.destroy)

        def open_user_manual():
            user_manual_path = res_path.resource_path('res/usermanual.pdf')
            webbrowser.open_new(user_manual_path)

        def open_process_manual():
            user_manual_path = res_path.resource_path('res/process_desc.pdf')
            webbrowser.open_new(user_manual_path)

