from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import res_path


class Gui:
    def __init__(self, root, radar_frame):
        self.root = root
        self.radar_frame = radar_frame

        self.ref_var = tk.StringVar()
        self.lat_var = tk.StringVar()
        self.lon_var = tk.StringVar()

        self.a_zr_var = tk.StringVar()
        self.b_zr_var = tk.StringVar()
        self.m_disd_var = tk.StringVar()
        self.b_disd_var = tk.StringVar()
        self.trunc_var = tk.StringVar()

        self.in_ref_to_pp_folder_path = tk.StringVar()
        self.out_ref_to_pp_folder_path = tk.StringVar()

        self.ref_to_pp_frame = ttk.Frame(self.radar_frame)
        self.ref_to_pp_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.ref_to_pp_frame.grid(row=1, column=0, sticky='nsew')

        self.ref_to_pp_title_frame = ttk.Frame(self.ref_to_pp_frame)
        self.ref_to_pp_title_frame.grid(row=0, column=0, sticky='nsew')

        self.ref_to_pp_title = ttk.Label(self.ref_to_pp_title_frame)
        self.ref_to_pp_title.configure(text="Precipitación a partir de reflectividad")
        self.ref_to_pp_title.grid(row=0, column=0, sticky='w')

        self.up_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/up_arrow.ico")))
        self.down_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/down_arrow.ico")))

        self.ref_to_pp_up_arrow = ttk.Label(self.ref_to_pp_title_frame, image=self.up_arrow)
        self.ref_to_pp_down_arrow = ttk.Label(self.ref_to_pp_title_frame, image=self.down_arrow)
        self.ref_to_pp_down_arrow.grid(row=0, column=1, sticky='e')

        self.ref_to_pp_frame_open = tk.BooleanVar()
        self.ref_to_pp_content = ttk.Frame(self.ref_to_pp_frame)
        self.ref_to_pp_frame_open.set(False)

        self.in_ref_to_pp_folder_label = ttk.Label(self.ref_to_pp_content)
        self.in_ref_to_pp_folder_label.configure(text="Carpeta de archivos nc")
        self.in_ref_to_pp_folder_label.grid(column=0, row=1)

        self.in_ref_to_pp_folder_entry = ttk.Entry(self.ref_to_pp_content)
        self.in_ref_to_pp_folder_entry.configure(cursor='arrow', width=27, textvariable=self.in_ref_to_pp_folder_path)
        self.in_ref_to_pp_folder_entry.grid(column=1, row=1, sticky='ew')

        self.in_ref_to_pp_folder_button = ttk.Button(self.ref_to_pp_content)
        self.in_ref_to_pp_folder_button.configure(text='...', width=5)
        self.in_ref_to_pp_folder_button.grid(column=2, row=1, sticky='e')

        self.lat_var_label = ttk.Label(self.ref_to_pp_content)
        self.lat_var_label.configure(text="Latitud")
        self.lat_var_label.grid(column=0, row=2)

        self.lat_var_combo = ttk.Combobox(self.ref_to_pp_content)
        self.lat_var.set("Seleccionar carpeta de nc")
        self.lat_var_combo.configure(cursor='arrow', exportselection=True, state='disabled',
                                     textvariable=self.lat_var)
        self.lat_var_combo.grid(column=1, row=2, columnspan=2, sticky='ew')

        self.lon_var_label = ttk.Label(self.ref_to_pp_content)
        self.lon_var_label.configure(text="Longitud")
        self.lon_var_label.grid(column=0, row=3)

        self.lon_var_combo = ttk.Combobox(self.ref_to_pp_content)
        self.lon_var.set("Seleccionar carpeta de nc")
        self.lon_var_combo.configure(cursor='arrow',
                                     exportselection=False,
                                     state='disabled',
                                     textvariable=self.lon_var)
        self.lon_var_combo.grid(column=1, row=3, columnspan=2, sticky='ew')

        self.ref_var_label = ttk.Label(self.ref_to_pp_content)
        self.ref_var_label.configure(text="Reflectividad")
        self.ref_var_label.grid(column=0, row=4)

        self.ref_var_combo = ttk.Combobox(self.ref_to_pp_content)
        self.ref_var.set("Seleccionar carpeta de nc")
        self.ref_var_combo.configure(cursor='arrow', exportselection=True, state='disabled',
                                     textvariable=self.ref_var)
        self.ref_var_combo.grid(column=1, row=4, columnspan=2, sticky='ew')

        self.out_ref_to_pp_folder_label = ttk.Label(self.ref_to_pp_content)
        self.out_ref_to_pp_folder_label.configure(text="Guardar en:")
        self.out_ref_to_pp_folder_label.grid(column=0, row=5)

        self.out_ref_to_pp_folder_entry = ttk.Entry(self.ref_to_pp_content)
        self.out_ref_to_pp_folder_entry.configure(cursor='arrow', width=27, textvariable=self.out_ref_to_pp_folder_path)
        self.out_ref_to_pp_folder_entry.grid(column=1, row=5, sticky='ew')

        self.out_ref_to_pp_folder_button = ttk.Button(self.ref_to_pp_content)
        self.out_ref_to_pp_folder_button.configure(text='...', width=5)
        self.out_ref_to_pp_folder_button.grid(column=2, row=5, sticky='e')

        self.ref_to_pp_config_button = ttk.Button(self.ref_to_pp_content)
        self.ref_to_pp_config_button.configure(text='Configuración modelo precipitación', width=5)
        self.ref_to_pp_config_button.grid(column=0, row=6, columnspan=3, sticky='ew')

        self.ref_to_pp_main_button = ttk.Button(self.ref_to_pp_content)
        self.ref_to_pp_main_button.configure(text='Ejecutar', width=5, state='disabled')
        self.ref_to_pp_main_button.grid(column=0, row=7, columnspan=3, sticky='ew')
