import tkinter as tk
import requests
import time
import out_textbox_write
from tkinter import ttk

class Window():
    def __init__(self, root, gui):

        self.root = root
        self.new_window = tk.Toplevel(self.root)
        self.gui = gui
        self.logged_in = self.gui.logged_in

        self.username = self.gui.username_var
        self.password = self.gui.password_var

        self.login_frame = ttk.Frame(self.new_window)
        self.login_frame.configure(padding=5)
        self.login_frame.grid(column=0, row=3)

        self.login_label = ttk.Label(self.login_frame)
        self.login_label.configure(text='Login EarthData')
        self.login_label.grid(column=0, row=0, columnspan=2)


        self.username_label = ttk.Label(self.login_frame)
        self.username_label.configure(text='Usuario')
        self.username_label.grid(column=0, row=1)

        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.configure(width=40, cursor='arrow', textvariable=self.username)
        self.username_entry.grid(column=1, row=1, sticky='w')

        self.password_label = ttk.Label(self.login_frame)
        self.password_label.configure(text='Contraseña')
        self.password_label.grid(column=0, row=2)

        self.password_entry = ttk.Entry(self.login_frame)
        self.password_entry.configure(width=40, cursor='arrow', textvariable=self.password)
        self.password_entry.grid(column=1, row=2, sticky='w')

        self.login_button = ttk.Button(self.login_frame)
        self.login_button.configure(text='Login')
        self.login_button.grid(row=3, column=0, columnspan=2, sticky='ew')

        self.login_check_label = ttk.Label(self.login_frame)


    def check_login(self):
        out_textbox_write.write(self.gui.out_textbox, 'Iniciando sesión...\n', True)
        self.root.update()
        server_url = 'https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3IMERGHH.06/2020/012/3B-HHR.MS.MRG.3IMERG.20200112-S000000-E002959.0000.V06B.HDF5.nc4'
        user = self.username.get()
        password = self.password.get()

        with requests.Session() as session:
            req = session.request('get', server_url)
            r = session.get(req.url, auth=(user, password))
            if r.status_code == 200:
                self.login_check_label.configure(text='Sesión iniciada')
                self.login_check_label.grid(row=4, column=0, columnspan=2)

                time.sleep(2)
                out_textbox_write.write(self.gui.out_textbox,'Sesion Iniciada Correctamente')

                self.new_window.destroy()
                self.logged_in.set(True)
            else:
                self.login_check_label.configure(text='Credenciales incorrectas, intente nuevamente')
                self.login_check_label.grid(row=4, column=0, columnspan=2)
                self.logged_in.set(False)
            self.root.update()

