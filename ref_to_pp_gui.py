from tkinter import ttk
import tkinter as tk


class Gui:
    def __init__(self,radar_gui):
        self.Radar_Panel = radar_gui

        self.Radar_Panel.in_ref_to_pp_folder_label = ttk.Label(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.in_ref_to_pp_folder_label.configure(text="Carpeta de archivos nc")
        self.Radar_Panel.in_ref_to_pp_folder_label.grid(column='0', row='1')

        self.Radar_Panel.in_ref_to_pp_folder_entry = ttk.Entry(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.in_ref_to_pp_folder_entry.configure(cursor='arrow', width='27', textvariable=self.Radar_Panel.in_ref_to_pp_folder_path)
        self.Radar_Panel.in_ref_to_pp_folder_entry.grid(column='1', row='1', sticky='ew')


        self.Radar_Panel.in_ref_to_pp_folder_button = ttk.Button(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.in_ref_to_pp_folder_button.configure(text='...', width='5')
        self.Radar_Panel.in_ref_to_pp_folder_button.grid(column='2', row='1', sticky='e')

        self.Radar_Panel.lat_var_label = ttk.Label(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.lat_var_label.configure(text="Latitud")
        self.Radar_Panel.lat_var_label.grid(column='0', row='2')

        self.Radar_Panel.lat_var_combo = ttk.Combobox(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.lat_var.set("Seleccionar carpeta de nc")
        self.Radar_Panel.lat_var_combo.configure(cursor='arrow', exportselection='true', state='disabled',
                                                 textvariable=self.Radar_Panel.lat_var)
        self.Radar_Panel.lat_var_combo.grid(column='1', row='2', columnspan='2', sticky='ew')

        self.Radar_Panel.lon_var_label = ttk.Label(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.lon_var_label.configure(text="Longitud")
        self.Radar_Panel.lon_var_label.grid(column='0', row='3')

        self.Radar_Panel.lon_var_combo = ttk.Combobox(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.lon_var.set("Seleccionar carpeta de nc")
        self.Radar_Panel.lon_var_combo.configure(cursor='arrow', exportselection='true', state='disabled',
                                                 textvariable=self.Radar_Panel.lon_var)
        self.Radar_Panel.lon_var_combo.grid(column='1', row='3', columnspan='2', sticky='ew')

        self.Radar_Panel.ref_var_label = ttk.Label(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.ref_var_label.configure(text="Reflectividad")
        self.Radar_Panel.ref_var_label.grid(column='0', row='4')

        self.Radar_Panel.ref_var_combo = ttk.Combobox(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.ref_var.set("Seleccionar carpeta de nc")
        self.Radar_Panel.ref_var_combo.configure(cursor='arrow', exportselection='true', state='disabled',
                                                 textvariable=self.Radar_Panel.ref_var)
        self.Radar_Panel.ref_var_combo.grid(column='1', row='4', columnspan='2', sticky='ew')


        self.Radar_Panel.out_ref_to_pp_folder_label = ttk.Label(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.out_ref_to_pp_folder_label.configure(text="Guardar en:")
        self.Radar_Panel.out_ref_to_pp_folder_label.grid(column='0', row='5')

        self.Radar_Panel.out_ref_to_pp_folder_entry = ttk.Entry(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.out_ref_to_pp_folder_entry.configure(cursor='arrow', width='27', textvariable=self.Radar_Panel.out_ref_to_pp_folder_path)
        self.Radar_Panel.out_ref_to_pp_folder_entry.grid(column='1', row='5', sticky='ew')


        self.Radar_Panel.out_ref_to_pp_folder_button = ttk.Button(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.out_ref_to_pp_folder_button.configure(text='...', width='5')
        self.Radar_Panel.out_ref_to_pp_folder_button.grid(column='2', row='5', sticky='e')


        self.Radar_Panel.ref_to_pp_config_button = ttk.Button(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.ref_to_pp_config_button.configure(text='Configuración modelo precipitación', width='5')
        self.Radar_Panel.ref_to_pp_config_button.grid(column='0', row='6', columnspan='3', sticky='ew')

        self.Radar_Panel.ref_to_pp_main_button = ttk.Button(self.Radar_Panel.ref_to_pp_content)
        self.Radar_Panel.ref_to_pp_main_button.configure(text='Ejecutar', width='5', state='disabled')
        self.Radar_Panel.ref_to_pp_main_button.grid(column='0', row='7', columnspan='3', sticky='ew')

