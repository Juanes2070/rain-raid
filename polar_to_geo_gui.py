from tkinter import ttk
import tkinter as tk


class Gui:
    def __init__(self, radar_gui):
        self.Radar_Panel = radar_gui

        self.Radar_Panel.in_polflat_folder_label = ttk.Label(self.Radar_Panel.pol_to_geo_content)
        self.Radar_Panel.in_polflat_folder_label.configure(text="Archivos de entrada")
        self.Radar_Panel.in_polflat_folder_label.grid(column='0', row='1')

        self.Radar_Panel.in_polflat_folder_entry = ttk.Entry(self.Radar_Panel.pol_to_geo_content)
        self.Radar_Panel.in_polflat_folder_entry.configure(cursor='arrow', width='27', textvariable=self.Radar_Panel.in_polflat_folder_path)
        self.Radar_Panel.in_polflat_folder_entry.grid(column='1', row='1', sticky='ew')
        self.Radar_Panel.in_polflat_folder_path.set('D:/Downloads/pyart_out/')

        self.Radar_Panel.in_polflat_folder_button = ttk.Button(self.Radar_Panel.pol_to_geo_content)
        self.Radar_Panel.in_polflat_folder_button.configure(text='...', width='5')
        self.Radar_Panel.in_polflat_folder_button.grid(column='2', row='1', sticky='e')

        self.Radar_Panel.out_polflat_folder_label = ttk.Label(self.Radar_Panel.pol_to_geo_content)
        self.Radar_Panel.out_polflat_folder_label.configure(text="Carpeta de salida")
        self.Radar_Panel.out_polflat_folder_label.grid(column='0', row='2')

        self.Radar_Panel.out_polflat_folder_entry = ttk.Entry(self.Radar_Panel.pol_to_geo_content)
        self.Radar_Panel.out_polflat_folder_entry.configure(cursor='arrow', width='27', textvariable=self.Radar_Panel.out_polflat_folder_path)
        self.Radar_Panel.out_polflat_folder_entry.grid(column='1', row='2', sticky='ew')
        self.Radar_Panel.out_polflat_folder_path.set('D:/Downloads/polar/')

        self.Radar_Panel.out_polflat_folder_button = ttk.Button(self.Radar_Panel.pol_to_geo_content)
        self.Radar_Panel.out_polflat_folder_button.configure(text='...', width='5')
        self.Radar_Panel.out_polflat_folder_button.grid(column='2', row='2', sticky='e')

        self.Radar_Panel.polflat_main_button = ttk.Button(self.Radar_Panel.pol_to_geo_content)
        self.Radar_Panel.polflat_main_button.configure(text='Ejecutar', width='5')
        self.Radar_Panel.polflat_main_button.grid(column='0', row='3', columnspan='3', sticky='ew')