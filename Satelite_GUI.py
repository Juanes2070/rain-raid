import tkinter as tk
import tkinter.ttk as ttk
import download_satellite_module


class Satelite_Elements:
    def __init__(self, root, frame):
        # Default values
        w_path_def = r"D:\Downloads\chirps_test/"
        mask_path_def = r"D:\GDrive\U\TESIS\SIG\Cartografía base\Esta_Extent.shp"

        self.root = root
        self.satellite_frame = frame

        # TODO bloquear el cuadro de texto
        self.out_textbox = tk.Text(self.satellite_frame)
        self.out_textbox.configure(background='#dddddd',
                                   cursor='arrow',
                                   relief='flat',
                                   height='10',
                                   width=42,
                                   state='disabled')
        self.out_textbox.grid(row=2, column=0, sticky='nsew', pady='5', padx='5')

        self.down_satellite_module = download_satellite_module.Module(self.root,
                                                                      self.satellite_frame,
                                                                      self.out_textbox)

        self.progressbar = ttk.Progressbar(self.satellite_frame)
        self.progressbar.configure(orient='horizontal')
        self.progressbar.grid(column=0, columnspan=2, row=3, sticky='ew')
