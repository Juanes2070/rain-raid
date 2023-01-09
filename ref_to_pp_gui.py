from tkinter import ttk
import tkinter as tk


class Gui:
    def __init__(self,radar_gui):
        self.radar_gui = radar_gui

        self.radar_gui.in_ref_to_pp_folder_label = ttk.Label(self.radar_gui.ref_to_pp_content)
        self.radar_gui.in_ref_to_pp_folder_label.configure(text="Carpeta de archivos nc")
        self.radar_gui.in_ref_to_pp_folder_label.grid(column='0', row='1')

        self.radar_gui.in_ref_to_pp_folder_entry = ttk.Entry(self.radar_gui.ref_to_pp_content)
        self.radar_gui.in_ref_to_pp_folder_entry.configure(cursor='arrow', width='27', textvariable=self.radar_gui.in_ref_to_pp_folder_path)
        self.radar_gui.in_ref_to_pp_folder_entry.grid(column='1', row='1', sticky='ew')


        self.radar_gui.in_ref_to_pp_folder_button = ttk.Button(self.radar_gui.ref_to_pp_content)
        self.radar_gui.in_ref_to_pp_folder_button.configure(text='...', width='5')
        self.radar_gui.in_ref_to_pp_folder_button.grid(column='2', row='1', sticky='e')

        self.radar_gui.lat_var_label = ttk.Label(self.radar_gui.ref_to_pp_content)
        self.radar_gui.lat_var_label.configure(text="Latitud")
        self.radar_gui.lat_var_label.grid(column='0', row='2')

        self.radar_gui.lat_var_combo = ttk.Combobox(self.radar_gui.ref_to_pp_content)
        self.radar_gui.lat_var.set("Seleccionar carpeta de nc")
        self.radar_gui.lat_var_combo.configure(cursor='arrow', exportselection='true', state='disabled',
                                     textvariable=self.radar_gui.lat_var)
        self.radar_gui.lat_var_combo.grid(column='1', row='2', columnspan='2', sticky='ew')

        self.radar_gui.lon_var_label = ttk.Label(self.radar_gui.ref_to_pp_content)
        self.radar_gui.lon_var_label.configure(text="Longitud")
        self.radar_gui.lon_var_label.grid(column='0', row='3')

        self.radar_gui.lon_var_combo = ttk.Combobox(self.radar_gui.ref_to_pp_content)
        self.radar_gui.lon_var.set("Seleccionar carpeta de nc")
        self.radar_gui.lon_var_combo.configure(cursor='arrow', exportselection='true', state='disabled',
                                     textvariable=self.radar_gui.lon_var)
        self.radar_gui.lon_var_combo.grid(column='1', row='3', columnspan='2', sticky='ew')

        self.radar_gui.ref_var_label = ttk.Label(self.radar_gui.ref_to_pp_content)
        self.radar_gui.ref_var_label.configure(text="Reflectividad")
        self.radar_gui.ref_var_label.grid(column='0', row='4')

        self.radar_gui.ref_var_combo = ttk.Combobox(self.radar_gui.ref_to_pp_content)
        self.radar_gui.ref_var.set("Seleccionar carpeta de nc")
        self.radar_gui.ref_var_combo.configure(cursor='arrow', exportselection='true', state='disabled',
                                     textvariable=self.radar_gui.ref_var)
        self.radar_gui.ref_var_combo.grid(column='1', row='4', columnspan='2', sticky='ew')


        self.radar_gui.out_ref_to_pp_folder_label = ttk.Label(self.radar_gui.ref_to_pp_content)
        self.radar_gui.out_ref_to_pp_folder_label.configure(text="Guardar en:")
        self.radar_gui.out_ref_to_pp_folder_label.grid(column='0', row='5')

        self.radar_gui.out_ref_to_pp_folder_entry = ttk.Entry(self.radar_gui.ref_to_pp_content)
        self.radar_gui.out_ref_to_pp_folder_entry.configure(cursor='arrow', width='27', textvariable=self.radar_gui.out_ref_to_pp_folder_path)
        self.radar_gui.out_ref_to_pp_folder_entry.grid(column='1', row='5', sticky='ew')


        self.radar_gui.out_ref_to_pp_folder_button = ttk.Button(self.radar_gui.ref_to_pp_content)
        self.radar_gui.out_ref_to_pp_folder_button.configure(text='...', width='5')
        self.radar_gui.out_ref_to_pp_folder_button.grid(column='2', row='5', sticky='e')


        self.radar_gui.ref_to_pp_config_button = ttk.Button(self.radar_gui.ref_to_pp_content)
        self.radar_gui.ref_to_pp_config_button.configure(text='Configuración modelo precipitación', width='5')
        self.radar_gui.ref_to_pp_config_button.grid(column='0', row='6', columnspan='3', sticky='ew')

        self.radar_gui.ref_to_pp_main_button = ttk.Button(self.radar_gui.ref_to_pp_content)
        self.radar_gui.ref_to_pp_main_button.configure(text='Ejecutar', width='5',state='disabled')
        self.radar_gui.ref_to_pp_main_button.grid(column='0', row='7', columnspan='3', sticky='ew')

        self.radar_gui.out_textbox = tk.Text(self.radar_gui.radar_frame)
        self.radar_gui.out_textbox.configure(background='#dddddd', relief='flat',height='10',width='42',state='disabled')
        self.radar_gui.out_textbox.grid(row='10',column='0',sticky='nsew',pady='5',padx='5')
