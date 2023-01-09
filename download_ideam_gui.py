import tkinter as tk
from tkinter import ttk
import tkcalendar


class Gui:
    def __init__(self, radar_panel):
        self.Radar_Panel = radar_panel

        self.Radar_Panel.period_radar_label = ttk.Label(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.period_radar_label.configure(text="Periodo de tiempo")
        self.Radar_Panel.period_radar_label.grid(row='1', column='0', sticky='w')

        self.Radar_Panel.start_date_entry = tkcalendar.DateEntry(self.Radar_Panel.download_ideam_content, locale='es_ES',
                                                                 date_pattern='dd/MM/yyyy')
        self.Radar_Panel.start_date_entry.configure(width='22', textvariable=self.Radar_Panel.start_date)
        self.Radar_Panel.start_date_entry.grid(column='0', row='2', sticky='ew')

        self.Radar_Panel.end_date_entry = tkcalendar.DateEntry(self.Radar_Panel.download_ideam_content, locale='es_ES',
                                                               date_pattern='dd/MM/yyyy')
        self.Radar_Panel.end_date_entry.configure(cursor='arrow', width='22', textvariable=self.Radar_Panel.end_date)
        self.Radar_Panel.end_date_entry.grid(column='0', row='3', sticky='ew')

        self.Radar_Panel.interval_frame = ttk.Frame(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.interval_frame.grid(row='4', column='0', sticky='ew', columnspan='2')

        self.Radar_Panel.interval_label = ttk.Label(self.Radar_Panel.interval_frame)
        self.Radar_Panel.interval_label.configure(text="Intevalo temporal:")
        self.Radar_Panel.interval_label.grid(row='0', column='0', sticky='w')

        self.Radar_Panel.interval_entry = ttk.Entry(self.Radar_Panel.interval_frame)
        self.Radar_Panel.interval_entry.configure(cursor='arrow', width='5', textvariable=self.Radar_Panel.interval)
        self.Radar_Panel.interval_entry.grid(row='0', column='1', sticky='e')

        self.Radar_Panel.interval_units_label = ttk.Label(self.Radar_Panel.interval_frame)
        self.Radar_Panel.interval_units_label.configure(text="min")
        self.Radar_Panel.interval_units_label.grid(row='0', column='3', sticky='w')

        self.Radar_Panel.avail_radar_button = ttk.Button(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.avail_radar_button.configure(text='Buscar', width='25')
        self.Radar_Panel.avail_radar_button.grid(row='5', column='0', sticky='ew')

        self.Radar_Panel.avail_radar_label = ttk.Label(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.avail_radar_label.configure(text="Radares disponibles:")
        self.Radar_Panel.avail_radar_label.grid(row='1', column='1', sticky='w')

        self.Radar_Panel.avail_radar_listbox = tk.Listbox(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.avail_radar_listbox.configure(background='#dddddd', height='3',
                                                       width='25',
                                                       relief='flat',
                                                       exportselection=False)
        self.Radar_Panel.avail_radar_listbox.grid(row='2', column='1', rowspan='4', sticky='nsew')

        self.Radar_Panel.format_save_label = ttk.Label(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.format_save_label.configure(text="Formato a guardar")
        self.Radar_Panel.format_save_label.grid(row='6', column='0', columnspan='2')

        self.Radar_Panel.save_raw_checkbox = tk.Checkbutton(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.save_raw_checkbox.configure(text='RAW', state='disabled', variable=self.Radar_Panel.save_raw_var)
        self.Radar_Panel.save_raw_checkbox.grid(row='7', column='0', sticky='w')

        self.Radar_Panel.save_nc_checkbox = tk.Checkbutton(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.save_nc_checkbox.configure(text='netCDF4', state='disabled', variable=self.Radar_Panel.save_nc_var)
        self.Radar_Panel.save_nc_checkbox.grid(row='8', column='0', sticky='w')

        self.Radar_Panel.save_tiff_checkbox = tk.Checkbutton(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.save_tiff_checkbox.configure(text='GeoTIFF (WGS84)', state='disabled',
                                                      variable=self.Radar_Panel.save_tiff_var)
        self.Radar_Panel.save_tiff_checkbox.grid(row='7', column='1', sticky='w')

        self.Radar_Panel.interp_options_select = ttk.Combobox(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.interp_options_select.configure(cursor='arrow', exportselection='true', state='disabled',
                                                         textvariable=self.Radar_Panel.interp_options)

        self.Radar_Panel.interp_options_select.configure(values='"No interpolar" "Nearest" "IDW" "Linear" "Kriging"')
        self.Radar_Panel.interp_options_select.grid(column='1', row='8', sticky='ew')

        self.Radar_Panel.download_route_frame = ttk.Frame(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.download_route_frame.grid(row='9', column='0', sticky='ew', columnspan='2')

        self.Radar_Panel.out_down_folder_label = ttk.Label(self.Radar_Panel.download_route_frame)
        self.Radar_Panel.out_down_folder_label.configure(text="Guardar en:")
        self.Radar_Panel.out_down_folder_label.grid(row='0', column='0')

        self.Radar_Panel.out_down_folder_entry = ttk.Entry(self.Radar_Panel.download_route_frame)
        self.Radar_Panel.out_down_folder_entry.configure(cursor='arrow', width='35',
                                                         textvariable=self.Radar_Panel.out_donwload_folder_path)
        self.Radar_Panel.out_down_folder_entry.grid(column='1', row='0', sticky='ew')

        self.Radar_Panel.out_down_folder_button = ttk.Button(self.Radar_Panel.download_route_frame)
        self.Radar_Panel.out_down_folder_button.configure(text='...', width='5')
        self.Radar_Panel.out_down_folder_button.grid(column='3', row='0', sticky='e')

        self.Radar_Panel.down_button = ttk.Button(self.Radar_Panel.download_ideam_content)
        self.Radar_Panel.down_button.configure(text='Descargar')
        self.Radar_Panel.down_button.grid(column='0', row='10', sticky='ew', columnspan='2')