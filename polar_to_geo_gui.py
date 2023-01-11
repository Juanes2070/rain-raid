import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import res_path


class Gui:
    def __init__(self, root, radar_frame):
        self.root = root
        self.radar_frame = radar_frame

        self.in_polflat_folder_path = tk.StringVar()
        self.out_polflat_folder_path = tk.StringVar()
        self.pol_to_geo_interpolate = tk.StringVar()

        self.pol_to_geo_frame = ttk.Frame(self.radar_frame)
        self.pol_to_geo_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.pol_to_geo_frame.grid(row=3, column=0, sticky='nsew')

        self.pol_to_geo_title_frame = ttk.Frame(self.pol_to_geo_frame)
        self.pol_to_geo_title_frame.grid(row=0, column=0, sticky='nsew')

        self.pol_to_geo_title = ttk.Label(self.pol_to_geo_title_frame)
        self.pol_to_geo_title.configure(text="Conversion de coordenadas polares a geográficas", cursor='hand2')
        self.pol_to_geo_title.grid(row=0, column=0, sticky='w')

        self.up_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/up_arrow.ico")))
        self.down_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/down_arrow.ico")))

        self.pol_to_geo_up_arrow = ttk.Label(self.pol_to_geo_title_frame, image=self.up_arrow)
        self.pol_to_geo_down_arrow = ttk.Label(self.pol_to_geo_title_frame, image=self.down_arrow)
        self.pol_to_geo_down_arrow.grid(row=0, column=1, sticky='e')

        self.pol_to_geo_frame_open = tk.BooleanVar()
        self.pol_to_geo_content = ttk.Frame(self.pol_to_geo_frame)
        self.pol_to_geo_frame_open.set(False)

        self.in_polflat_folder_label = ttk.Label(self.pol_to_geo_content)
        self.in_polflat_folder_label.configure(text="Carpeta archivos netCDF4")
        self.in_polflat_folder_label.grid(column=0, row=1)

        self.in_polflat_folder_entry = ttk.Entry(self.pol_to_geo_content)
        self.in_polflat_folder_entry.configure(cursor='arrow', width=25,
                                                           textvariable=self.in_polflat_folder_path)
        self.in_polflat_folder_entry.grid(column=1, row=1, sticky='ew')

        self.in_polflat_folder_button = ttk.Button(self.pol_to_geo_content)
        self.in_polflat_folder_button.configure(text='...', width=5)
        self.in_polflat_folder_button.grid(column=2, row=1, sticky='e')

        self.polflat_interpolate_label = ttk.Label(self.pol_to_geo_content)
        self.polflat_interpolate_label.configure(text="Interpolación")
        self.polflat_interpolate_label.grid(column=0, row=2)

        self.pol_to_geo_interpolate_select = ttk.Combobox(self.pol_to_geo_content)
        self.pol_to_geo_interpolate_select.configure(cursor='arrow',
                                                                 exportselection=True,
                                                                 textvariable=self.pol_to_geo_interpolate)

        self.pol_to_geo_interpolate_select.configure(values='"No interpolar" "Nearest" "IDW" "Linear" "Kriging"')
        self.pol_to_geo_interpolate_select.grid(column=1, row=2, sticky='ew',columnspan=2)
        self.pol_to_geo_interpolate.set("No interpolar")

        self.polflat_main_button = ttk.Button(self.pol_to_geo_content)
        self.polflat_main_button.configure(text='Ejecutar', width=5)
        self.polflat_main_button.grid(column=0, row=3, columnspan=3, sticky='ew')
