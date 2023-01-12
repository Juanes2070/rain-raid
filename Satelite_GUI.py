import tkinter as tk
import tkinter.ttk as ttk
import download_satellite_module
import default_values

class Satelite_Elements:
    def __init__(self, root, frame):
        self.root = root
        self.satellite_frame = frame

        # TODO bloquear el cuadro de texto
        self.out_textbox = tk.Text(self.satellite_frame)
        self.out_textbox.configure(background='#dddddd',
                                   cursor='arrow',
                                   relief='flat',
                                   state='disabled')
        self.out_textbox.grid(row=2, column=0, sticky='nsew', pady='5', padx='5')

        self.down_satellite_module = download_satellite_module.Module(self.root,
                                                                      self.satellite_frame,
                                                                      self.out_textbox)


        default_values.set_sat_default_values(self)
