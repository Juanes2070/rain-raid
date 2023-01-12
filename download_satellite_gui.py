import tkinter as tk
from tkinter import ttk
import tkcalendar
from PIL import ImageTk, Image
from hover_info import CreateToolTip
import res_path


class Gui:
    def __init__(self, root, sat_frame):

        self.root = root
        self.sat_frame = sat_frame

        self.out_folder_path = tk.StringVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.mission = tk.StringVar()

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.download_satellite_frame = ttk.Frame(self.sat_frame)
        self.download_satellite_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.download_satellite_frame.grid(row=0, column=0, sticky='nsew')

        self.download_satellite_frame_open = tk.BooleanVar()
        self.download_satellite_content = ttk.Frame(self.download_satellite_frame)
        self.download_satellite_frame_open.set(False)

        self.download_satellite_title_frame = ttk.Frame(self.download_satellite_frame)
        self.download_satellite_title_frame.grid(row=0, column=0, sticky='nsew')

        self.download_title = ttk.Label(self.download_satellite_title_frame)
        self.download_title.configure(text="Descarga Satélite", cursor='hand2')
        self.download_title.grid(row=0, column=0)

        self.up_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/up_arrow.ico")))
        self.down_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/down_arrow.ico")))

        self.satellite_up_arrow = ttk.Label(self.download_satellite_title_frame, image=self.up_arrow)
        self.satellite_down_arrow = ttk.Label(self.download_satellite_title_frame, image=self.down_arrow)
        self.satellite_down_arrow.grid(row=0, column=1, sticky='e')

        self.input_parameters_frame = ttk.Frame(self.download_satellite_content)
        self.input_parameters_frame.grid(column=0, row=0)

        self.mission_select_frame = ttk.Frame(self.input_parameters_frame)
        self.mission_select_frame.grid(row=1,column=1)

        self.mission_label = ttk.Label(self.mission_select_frame)
        self.mission_label.configure(text='Misión')
        self.mission_label.grid(column=0, row=0, sticky='w')



        self.mission_select = ttk.Combobox(self.mission_select_frame)
        self.mission_select.configure(width=24,
                                      cursor='arrow',
                                      state='readonly',
                                      textvariable=self.mission)

        # TODO colocar los nombres completos de las misiones
        self.mission_select.configure(values='"IMERG" "CHIRPS"')
        self.mission_select.set("IMERG")
        self.mission_select.grid(column=0, row=1, sticky='ew')

        self.login_button = ttk.Button(self.mission_select_frame)
        self.login_button.configure(text='EarthData Login')
        self.login_button.grid(row=2, column=0 ,columnspan=2, sticky='ew')

        self.down_date_frame = ttk.Frame(self.input_parameters_frame)
        self.down_date_frame.grid(row=1, column=0, sticky='w')

        self.period_radar_label = ttk.Label(self.down_date_frame)
        self.period_radar_label.configure(text="Periodo de tiempo")
        self.period_radar_label.grid(row=0, column=0, sticky='w', columnspan=2)

        self.start_date_label = ttk.Label(self.down_date_frame)
        self.start_date_label.configure(text='Fecha inicial')
        self.start_date_label.grid(row=1, column=0, sticky='w')

        self.start_date_entry = tkcalendar.DateEntry(self.down_date_frame,
                                                     locale='es_ES',
                                                     date_pattern='dd/MM/yyyy')
        self.start_date_entry.configure(textvariable=self.start_date)
        self.start_date_entry.grid(row=1, column=1, sticky='w')

        self.end_date_label = ttk.Label(self.down_date_frame)
        self.end_date_label.configure(text='Fecha final')
        self.end_date_label.grid(row=2, column=0, sticky='w')

        self.end_date_entry = tkcalendar.DateEntry(self.down_date_frame,
                                                   locale='es_ES',
                                                   date_pattern='dd/MM/yyyy')
        self.end_date_entry.configure(cursor='arrow', textvariable=self.end_date)
        self.end_date_entry.grid(row=2, column=1, sticky='w')

        self.download_folder_frame = ttk.Frame(self.input_parameters_frame)
        self.download_folder_frame.grid(row=3, column=0,columnspan=2, sticky='w')

        self.out_folder_label = ttk.Label(self.download_folder_frame)
        self.out_folder_label.configure(text='Guardar en')
        self.out_folder_label.grid(column=0, row=0, sticky='e')

        self.out_folder_entry = ttk.Entry(self.download_folder_frame)
        self.out_folder_entry.configure(width=38, textvariable=self.out_folder_path)
        self.out_folder_entry.grid(column=1, row=0, sticky='ew')

        self.out_folder_button = ttk.Button(self.download_folder_frame)
        self.out_folder_button.configure(text='...', width=5)
        self.out_folder_button.grid(column=2, row=0, sticky='w')

        self.main_button = ttk.Button(self.input_parameters_frame)
        self.main_button.configure(text='Descargar')
        self.main_button.grid(column=0, row=4, columnspan=2, sticky='ew')








