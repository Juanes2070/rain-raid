import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk,Image
import tkcalendar
import default_values
import res_path

class Radar_Elements:
    def __init__(self, root, frame):

        self.root = root
        self.radar_frame = frame

        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.interval = tk.StringVar()
        self.selected_radar = tk.StringVar()

        self.save_raw_var = tk.BooleanVar()
        self.save_nc_var = tk.BooleanVar()
        self.save_tiff_var = tk.BooleanVar()
        self.out_donwload_folder_path = tk.StringVar()

        self.ref_var = tk.StringVar()
        self.lat_var = tk.StringVar()
        self.lon_var = tk.StringVar()

        self.a_zr_var = tk.StringVar()
        self.b_zr_var = tk.StringVar()
        self.m_disd_var = tk.StringVar()
        self.b_disd_var = tk.StringVar()
        self.trunc_var = tk.StringVar()

        self.in_polflat_folder_path = tk.StringVar()
        self.out_polflat_folder_path = tk.StringVar()
        self.in_raw_to_nc_folder_path = tk.StringVar()
        self.out_raw_to_nc_folder_path = tk.StringVar()
        self.in_ref_to_pp_folder_path = tk.StringVar()
        self.out_ref_to_pp_folder_path = tk.StringVar()
        self.interp_options = tk.StringVar()


        self.in_folder_path = tk.StringVar()

        self.coord_sys = tk.StringVar()


        self.download_ideam_frame = ttk.Frame(self.radar_frame)
        self.download_ideam_frame.configure(borderwidth ='1', relief='ridge', padding='5')
        self.download_ideam_frame.grid(row='0', column='0', sticky='nsew')

        self.dowload_ideam_frame_open = tk.BooleanVar()
        self.download_ideam_content = ttk.Frame(self.download_ideam_frame)
        self.dowload_ideam_frame_open.set(False)

        self.download_ideam_title_frame = ttk.Frame(self.download_ideam_frame)
        self.download_ideam_title_frame.grid(row='0',column='0',sticky='nsew')

        self.download_title = ttk.Label(self.download_ideam_title_frame)
        self.download_title.configure(text="Descarga-IDEAM")
        self.download_title.grid(row='0',column='0')

        self.up_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/up_arrow.ico")))
        self.down_arrow = ImageTk.PhotoImage(Image.open(res_path.resource_path("img/down_arrow.ico")))

        self.ideam_up_arrow = ttk.Label(self.download_ideam_title_frame,image=self.up_arrow)
        self.ideam_down_arrow = ttk.Label(self.download_ideam_title_frame, image=self.down_arrow)
        self.ideam_down_arrow.grid(row='0',column='1',sticky='e')



        # ---------------------------------------------------------------------------------------------------------------

        self.ref_to_pp_frame = ttk.Frame(self.radar_frame)
        self.ref_to_pp_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.ref_to_pp_frame.grid(row='1', column='0', sticky='nsew')

        self.ref_to_pp_title_frame = ttk.Frame(self.ref_to_pp_frame)
        self.ref_to_pp_title_frame.grid(row='0', column='0', sticky='nsew')

        self.ref_to_pp_title = ttk.Label(self.ref_to_pp_title_frame)
        self.ref_to_pp_title.configure(text="Precipitación a partir de reflectividad")
        self.ref_to_pp_title.grid(row='0', column='0', sticky='w')

        self.ref_to_pp_up_arrow = ttk.Label(self.ref_to_pp_title_frame, image=self.up_arrow)
        self.ref_to_pp_down_arrow = ttk.Label(self.ref_to_pp_title_frame, image=self.down_arrow)
        self.ref_to_pp_down_arrow.grid(row='0', column='1', sticky='e')

        self.ref_to_pp_frame_open = tk.BooleanVar()
        self.ref_to_pp_content = ttk.Frame(self.ref_to_pp_frame)
        self.ref_to_pp_frame_open.set(False)



        #----------------------------------------------------------------------------------------------

        self.raw_to_nc_frame = ttk.Frame(self.radar_frame)
        self.raw_to_nc_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.raw_to_nc_frame.grid(row='2', column='0', sticky='nsew')

        self.raw_to_nc_title_frame = ttk.Frame(self.raw_to_nc_frame)
        self.raw_to_nc_title_frame.grid(row='0', column='0', sticky='nsew')

        self.raw_to_nc_title = ttk.Label(self.raw_to_nc_title_frame)
        self.raw_to_nc_title.configure(text="Conversion de RAW a netCDF4")
        self.raw_to_nc_title.grid(row='0', column='0', sticky='w')

        self.raw_to_nc_up_arrow = ttk.Label(self.raw_to_nc_title_frame, image=self.up_arrow)
        self.raw_to_nc_down_arrow = ttk.Label(self.raw_to_nc_title_frame, image=self.down_arrow)
        self.raw_to_nc_down_arrow.grid(row='0', column='1', sticky='e')

        self.raw_to_nc_frame_open = tk.BooleanVar()
        self.raw_to_nc_content = ttk.Frame(self.raw_to_nc_frame)
        self.raw_to_nc_frame_open.set(False)

        # ----------------------------------------------------------------------------------------------

        self.pol_to_geo_frame = ttk.Frame(self.radar_frame)
        self.pol_to_geo_frame.configure(borderwidth='1', relief='ridge', padding='5')
        self.pol_to_geo_frame.grid(row='3', column='0', sticky='nsew')

        self.pol_to_geo_title_frame = ttk.Frame(self.pol_to_geo_frame)
        self.pol_to_geo_title_frame.grid(row='0', column='0', sticky='nsew')

        self.pol_to_geo_title = ttk.Label(self.pol_to_geo_title_frame)
        self.pol_to_geo_title.configure(text="Conversion de coordenadas polares a geográficas")
        self.pol_to_geo_title.grid(row='0', column='0', sticky='w')

        self.pol_to_geo_up_arrow = ttk.Label(self.pol_to_geo_title_frame, image=self.up_arrow)
        self.pol_to_geo_down_arrow = ttk.Label(self.pol_to_geo_title_frame, image=self.down_arrow)
        self.pol_to_geo_down_arrow.grid(row='0', column='1', sticky='e')

        self.pol_to_geo_frame_open = tk.BooleanVar()
        self.pol_to_geo_content = ttk.Frame(self.pol_to_geo_frame)
        self.pol_to_geo_frame_open.set(False)

        default_values.set_default_values(self)



