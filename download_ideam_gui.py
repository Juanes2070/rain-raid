import tkinter as tk
from tkinter import ttk
import tkcalendar

class Gui:
    def __init__(self,radar_gui):
        self.radar_gui = radar_gui

        self.radar_gui.period_radar_label = ttk.Label(self.radar_gui.download_ideam_content)
        self.radar_gui.period_radar_label.configure(text="Periodo de tiempo")
        self.radar_gui.period_radar_label.grid(row='1', column='0', sticky='w')

        self.radar_gui.start_date_entry = tkcalendar.DateEntry(self.radar_gui.download_ideam_content, locale='es_ES',
                                                               date_pattern='dd/MM/yyyy')
        self.radar_gui.start_date_entry.configure(width='22', textvariable=self.radar_gui.start_date)
        self.radar_gui.start_date_entry.grid(column='0', row='2', sticky='ew')

        self.radar_gui.end_date_entry = tkcalendar.DateEntry(self.radar_gui.download_ideam_content, locale='es_ES',
                                                             date_pattern='dd/MM/yyyy')
        self.radar_gui.end_date_entry.configure(cursor='arrow', width='22', textvariable=self.radar_gui.end_date)
        self.radar_gui.end_date_entry.grid(column='0', row='3', sticky='ew')

        self.radar_gui.interval_frame = ttk.Frame(self.radar_gui.download_ideam_content)
        self.radar_gui.interval_frame.grid(row='4', column='0', sticky='ew', columnspan='2')

        self.radar_gui.interval_label = ttk.Label(self.radar_gui.interval_frame)
        self.radar_gui.interval_label.configure(text="Intevalo temporal:")
        self.radar_gui.interval_label.grid(row='0', column='0', sticky='w')

        self.radar_gui.interval_entry = ttk.Entry(self.radar_gui.interval_frame)
        self.radar_gui.interval_entry.configure(cursor='arrow', width='5', textvariable=self.radar_gui.interval)
        self.radar_gui.interval_entry.grid(row='0', column='1', sticky='e')

        self.radar_gui.interval_units_label = ttk.Label(self.radar_gui.interval_frame)
        self.radar_gui.interval_units_label.configure(text="min")
        self.radar_gui.interval_units_label.grid(row='0', column='3', sticky='w')

        self.radar_gui.avail_radar_button = ttk.Button(self.radar_gui.download_ideam_content)
        self.radar_gui.avail_radar_button.configure(text='Buscar', width='25')
        self.radar_gui.avail_radar_button.grid(row='5', column='0', sticky='ew')

        self.radar_gui.avail_radar_label = ttk.Label(self.radar_gui.download_ideam_content)
        self.radar_gui.avail_radar_label.configure(text="Radares disponibles:")
        self.radar_gui.avail_radar_label.grid(row='1', column='1', sticky='w')

        self.radar_gui.avail_radar_listbox = tk.Listbox(self.radar_gui.download_ideam_content)
        self.radar_gui.avail_radar_listbox.configure(background='#dddddd', height='3',
                                                     width='25',
                                                     relief='flat')
        self.radar_gui.avail_radar_listbox.grid(row='2', column='1', rowspan='4', sticky='nsew')

        self.radar_gui.format_save_label = ttk.Label(self.radar_gui.download_ideam_content)
        self.radar_gui.format_save_label.configure(text="Formato a guardar")
        self.radar_gui.format_save_label.grid(row='6', column='0', columnspan='2')

        self.radar_gui.save_raw_checkbox = tk.Checkbutton(self.radar_gui.download_ideam_content)
        self.radar_gui.save_raw_checkbox.configure(text='RAW', state='disabled', variable=self.radar_gui.save_raw_var)
        self.radar_gui.save_raw_checkbox.grid(row='7', column='0', sticky='w')

        self.radar_gui.save_nc_checkbox = tk.Checkbutton(self.radar_gui.download_ideam_content)
        self.radar_gui.save_nc_checkbox.configure(text='netCDF4', state='disabled', variable=self.radar_gui.save_nc_var)
        self.radar_gui.save_nc_checkbox.grid(row='8', column='0', sticky='w')

        self.radar_gui.save_tiff_checkbox = tk.Checkbutton(self.radar_gui.download_ideam_content)
        self.radar_gui.save_tiff_checkbox.configure(text='GeoTIFF (WGS84)', state='disabled',
                                                    variable=self.radar_gui.save_tiff_var)
        self.radar_gui.save_tiff_checkbox.grid(row='7', column='1', sticky='w')

        self.radar_gui.interp_options_select = ttk.Combobox(self.radar_gui.download_ideam_content)
        self.radar_gui.interp_options_select.configure(cursor='arrow', exportselection='true', state='disabled',
                                                       textvariable=self.radar_gui.interp_options)

        self.radar_gui.interp_options_select.configure(values='"No interpolar" "Nearest" "IDW" "Linear" "Kriging"')
        self.radar_gui.interp_options_select.grid(column='1', row='8', sticky='ew')

        self.radar_gui.download_route_frame = ttk.Frame(self.radar_gui.download_ideam_content)
        self.radar_gui.download_route_frame.grid(row='9', column='0', sticky='ew', columnspan='2')

        self.radar_gui.out_down_folder_label = ttk.Label(self.radar_gui.download_route_frame)
        self.radar_gui.out_down_folder_label.configure(text="Guardar en:")
        self.radar_gui.out_down_folder_label.grid(row='0', column='0')

        self.radar_gui.out_down_folder_entry = ttk.Entry(self.radar_gui.download_route_frame)
        self.radar_gui.out_down_folder_entry.configure(cursor='arrow', width='35',
                                                       textvariable=self.radar_gui.out_donwload_folder_path)
        self.radar_gui.out_down_folder_entry.grid(column='1', row='0', sticky='ew')

        self.radar_gui.out_down_folder_button = ttk.Button(self.radar_gui.download_route_frame)
        self.radar_gui.out_down_folder_button.configure(text='...', width='5')
        self.radar_gui.out_down_folder_button.grid(column='3', row='0', sticky='e')

        self.radar_gui.down_button = ttk.Button(self.radar_gui.download_ideam_content)
        self.radar_gui.down_button.configure(text='Descargar')
        self.radar_gui.down_button.grid(column='0', row='10', sticky='ew', columnspan='2')