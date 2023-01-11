from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import res_path


class Gui:
    def __init__(self, root, radar_frame):
        self.root = root
        self.radar_frame = radar_frame

        self.in_raw_to_nc_folder_path = tk.StringVar()
        self.out_raw_to_nc_folder_path = tk.StringVar()
        self.raw_to_nc_conversion = tk.BooleanVar()
        self.raw_to_nc_interpolate = tk.StringVar()

        self.raw_to_nc_frame = ttk.Frame(self.radar_frame)
        self.raw_to_nc_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.raw_to_nc_frame.grid(row=2, column=0, sticky='nsew')

        self.raw_to_nc_title_frame = ttk.Frame(self.raw_to_nc_frame)
        self.raw_to_nc_title_frame.grid(row=0, column=0, sticky='nsew')

        self.raw_to_nc_title = ttk.Label(self.raw_to_nc_title_frame)
        self.raw_to_nc_title.configure(text="Conversion de RAW a netCDF4", cursor='hand2')
        self.raw_to_nc_title.grid(row=0, column=0, sticky='w')

        self.up_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/up_arrow.ico")))
        self.down_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/down_arrow.ico")))

        self.raw_to_nc_up_arrow = ttk.Label(self.raw_to_nc_title_frame, image=self.up_arrow)
        self.raw_to_nc_down_arrow = ttk.Label(self.raw_to_nc_title_frame, image=self.down_arrow)
        self.raw_to_nc_down_arrow.grid(row=0, column=1, sticky='e')

        self.raw_to_nc_frame_open = tk.BooleanVar()
        self.raw_to_nc_content = ttk.Frame(self.raw_to_nc_frame)
        self.raw_to_nc_frame_open.set(False)

        self.in_raw_to_nc_folder_label = ttk.Label(self.raw_to_nc_content)

        self.in_raw_to_nc_folder_label.configure(text="Carpeta de archivos RAW:")
        self.in_raw_to_nc_folder_label.grid(column=0, row=1, sticky='w')

        self.in_raw_to_nc_folder_entry = ttk.Entry(self.raw_to_nc_content)
        self.in_raw_to_nc_folder_entry.configure(cursor='arrow', width=48,
                                                 textvariable=self.in_raw_to_nc_folder_path)
        self.in_raw_to_nc_folder_entry.grid(column=0, row=2, sticky='ew')

        self.in_raw_to_nc_folder_button = ttk.Button(self.raw_to_nc_content)
        self.in_raw_to_nc_folder_button.configure(text='...', width=5)
        self.in_raw_to_nc_folder_button.grid(column=1, row=2, sticky='e')

        self.out_raw_to_nc_folder_label = ttk.Label(self.raw_to_nc_content)
        self.out_raw_to_nc_folder_label.configure(text="Guardar en:")
        self.out_raw_to_nc_folder_label.grid(column=0, row=3, sticky='w')

        self.out_raw_to_nc_folder_entry = ttk.Entry(self.raw_to_nc_content)
        self.out_raw_to_nc_folder_entry.configure(cursor='arrow', width=48,
                                                  textvariable=self.out_raw_to_nc_folder_path)
        self.out_raw_to_nc_folder_entry.grid(column=0, row=4, sticky='ew')

        self.out_raw_to_nc_folder_button = ttk.Button(self.raw_to_nc_content)
        self.out_raw_to_nc_folder_button.configure(text='...', width=5)
        self.out_raw_to_nc_folder_button.grid(column=1, row=4, sticky='e')

        self.pol_flat_conversion_frame = ttk.Frame(self.raw_to_nc_content)
        self.pol_flat_conversion_frame.grid(row=5, column=0, sticky='w', columnspan=2)

        self.nc_conversion_checkbox = ttk.Checkbutton(self.pol_flat_conversion_frame)
        self.nc_conversion_checkbox.configure(text='Convertir a sistema geográfico',
                                              variable=self.raw_to_nc_conversion)
        self.nc_conversion_checkbox.grid(row=0, column=0, sticky='w')

        self.nc_interp_options_select = ttk.Combobox(self.pol_flat_conversion_frame)
        self.nc_interp_options_select.configure(cursor='arrow',
                                                exportselection=True,
                                                state='disabled',
                                                textvariable=self.raw_to_nc_interpolate)

        self.nc_interp_options_select.configure(values='"No interpolar" "Nearest" "IDW" "Linear" "Kriging"')
        self.nc_interp_options_select.grid(column=1, row=0, sticky='ew')
        self.raw_to_nc_interpolate.set("No interpolar")

        self.raw_to_nc_main_button = ttk.Button(self.raw_to_nc_content)
        self.raw_to_nc_main_button.configure(text='Ejecutar', width=5)
        self.raw_to_nc_main_button.grid(column=0, row=6, columnspan=3, sticky='ew')
