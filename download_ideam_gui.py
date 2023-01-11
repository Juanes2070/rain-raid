import tkinter as tk
from tkinter import ttk
import tkcalendar
from PIL import ImageTk, Image
import res_path


class Gui:
    def __init__(self, root, radar_frame):

        self.root = root

        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.interval = tk.StringVar()
        self.selected_radar = tk.StringVar()

        self.save_raw_var = tk.BooleanVar()
        self.save_nc_var = tk.BooleanVar()
        self.save_tiff_var = tk.BooleanVar()
        self.out_download_folder_path = tk.StringVar()

        self.interp_options = tk.StringVar()

        self.radar_frame = radar_frame

        self.download_ideam_frame = ttk.Frame(self.radar_frame)
        self.download_ideam_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.download_ideam_frame.grid(row=0, column=0, sticky='nsew')

        self.dowload_ideam_frame_open = tk.BooleanVar()
        self.download_ideam_content = ttk.Frame(self.download_ideam_frame)
        self.dowload_ideam_frame_open.set(False)

        self.download_ideam_title_frame = ttk.Frame(self.download_ideam_frame)
        self.download_ideam_title_frame.grid(row=0, column=0, sticky='nsew')

        self.download_title = ttk.Label(self.download_ideam_title_frame)
        self.download_title.configure(text="Descarga-IDEAM")
        self.download_title.grid(row=0, column=0)

        self.up_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/up_arrow.ico")))
        self.down_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/down_arrow.ico")))

        self.ideam_up_arrow = ttk.Label(self.download_ideam_title_frame, image=self.up_arrow)
        self.ideam_down_arrow = ttk.Label(self.download_ideam_title_frame, image=self.down_arrow)
        self.ideam_down_arrow.grid(row=0, column=1, sticky='e')

        # TODO Colocar fecha inicial y final :)
        self.period_radar_label = ttk.Label(self.download_ideam_content)
        self.period_radar_label.configure(text="Periodo de tiempo")
        self.period_radar_label.grid(row=1, column=0, sticky='w')

        self.start_date_entry = tkcalendar.DateEntry(self.download_ideam_content, locale='es_ES',
                                                     date_pattern='dd/MM/yyyy')
        self.start_date_entry.configure(width='22', textvariable=self.start_date)
        self.start_date_entry.grid(column=0, row=2, sticky='ew')

        self.end_date_entry = tkcalendar.DateEntry(self.download_ideam_content, locale='es_ES',
                                                   date_pattern='dd/MM/yyyy')
        self.end_date_entry.configure(cursor='arrow', width='22', textvariable=self.end_date)
        self.end_date_entry.grid(column=0, row=3, sticky='ew')

        self.interval_frame = ttk.Frame(self.download_ideam_content)
        self.interval_frame.grid(row=4, column=0, sticky='ew', columnspan=2)

        self.interval_label = ttk.Label(self.interval_frame)
        self.interval_label.configure(text="Intevalo temporal:")
        self.interval_label.grid(row=0, column=0, sticky='w')

        self.interval_entry = ttk.Entry(self.interval_frame)
        self.interval_entry.configure(cursor='arrow', width=5, textvariable=self.interval)
        self.interval_entry.grid(row=0, column=1, sticky='e')

        self.interval_units_label = ttk.Label(self.interval_frame)
        self.interval_units_label.configure(text="min")
        self.interval_units_label.grid(row=0, column=3, sticky='w')

        self.avail_radar_button = ttk.Button(self.download_ideam_content)
        self.avail_radar_button.configure(text='Buscar', width=25)
        self.avail_radar_button.grid(row=5, column=0, sticky='ew')

        self.avail_radar_label = ttk.Label(self.download_ideam_content)
        self.avail_radar_label.configure(text="Radares disponibles:")
        self.avail_radar_label.grid(row=1, column=1, sticky='w')

        self.avail_radar_listbox = tk.Listbox(self.download_ideam_content)
        self.avail_radar_listbox.configure(background='#dddddd', height=3,
                                           width=25,
                                           relief='flat',
                                           exportselection=False)
        self.avail_radar_listbox.grid(row=2, column=1, rowspan=4, sticky='nsew')

        self.format_save_label = ttk.Label(self.download_ideam_content)
        self.format_save_label.configure(text="Formato a guardar")
        self.format_save_label.grid(row=6, column=0, columnspan=2)

        self.save_raw_checkbox = tk.Checkbutton(self.download_ideam_content)
        self.save_raw_checkbox.configure(text='RAW', state='disabled', variable=self.save_raw_var)
        self.save_raw_checkbox.grid(row=7, column=0, sticky='w')

        self.save_nc_checkbox = tk.Checkbutton(self.download_ideam_content)
        self.save_nc_checkbox.configure(text='netCDF4', state='disabled', variable=self.save_nc_var)
        self.save_nc_checkbox.grid(row=8, column=0, sticky='w')

        self.save_tiff_checkbox = tk.Checkbutton(self.download_ideam_content)
        self.save_tiff_checkbox.configure(text='GeoTIFF (WGS84)', state='disabled',
                                          variable=self.save_tiff_var)
        self.save_tiff_checkbox.grid(row=7, column=1, sticky='w')

        self.interp_options_select = ttk.Combobox(self.download_ideam_content)
        self.interp_options_select.configure(cursor='arrow', exportselection=True, state='disabled',
                                             textvariable=self.interp_options)

        self.interp_options_select.configure(values='"No interpolar" "Nearest" "IDW" "Linear" "Kriging"')
        self.interp_options_select.grid(column=1, row=8, sticky='ew')

        self.download_route_frame = ttk.Frame(self.download_ideam_content)
        self.download_route_frame.grid(row=9, column=0, sticky='ew', columnspan=2)

        self.out_down_folder_label = ttk.Label(self.download_route_frame)
        self.out_down_folder_label.configure(text="Guardar en:")
        self.out_down_folder_label.grid(row=0, column=0)

        self.out_down_folder_entry = ttk.Entry(self.download_route_frame)
        self.out_down_folder_entry.configure(cursor='arrow', width=35,
                                             textvariable=self.out_download_folder_path)
        self.out_down_folder_entry.grid(column=1, row=0, sticky='ew')

        self.out_down_folder_button = ttk.Button(self.download_route_frame)
        self.out_down_folder_button.configure(text='...', width=5)
        self.out_down_folder_button.grid(column=3, row=0, sticky='e')

        self.down_button = ttk.Button(self.download_ideam_content)
        self.down_button.configure(text='Descargar')
        self.down_button.grid(column=0, row=10, sticky='ew', columnspan=2)
