import tkinter as tk
import tkinter.ttk as ttk
import Satelite_GUI
import Radar_GUI
import Radar_functions_2
import Satellite_Functions
import ref_to_pp_settings_window
import raw_to_nc_gui
import download_ideam_gui
import ref_to_pp_gui
import polar_to_geo_gui


class MainWindow:
    def __init__(self, master=None):
        # Main notebook
        self.root = tk.Tk(master)  # Makes the window
        self.root.wm_title("Rain-raid")  # Makes the title that will appear in the top left
        self.root.config(background="#FFFFFF")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        # self.radar_frame = ttk.Frame(self.notebook)
        self.radar_frame2 = ttk.Frame(self.notebook)
        self.sat_frame = ttk.Frame(self.notebook)

        # self.RadarPanel = Radar_GUI.Radar_Elements(self.root, self.radar_frame)
        self.Sat_Panel = Satelite_GUI.Satelite_Elements(self.root, self.sat_frame)
        self.Radar_Panel = Radar_GUI.Radar_Elements(self.root, self.radar_frame2)

        # self.notebook.add(self.radar_frame, text='Radar')
        self.notebook.add(self.radar_frame2, text='Radar Tools')

        # self.notebook.add(self.sat_frame, text='Satellite')

        def miss_click(*args):
            Satellite_Functions.mission_click(self.Sat_Panel)

        self.raw_to_nc_gui = raw_to_nc_gui.Gui(self.Radar_Panel)
        self.ideam_gui = download_ideam_gui.Gui(self.Radar_Panel)
        self.ref_to_pp_gui = ref_to_pp_gui.Gui(self.Radar_Panel)
        self.pol_to_geo_gui = polar_to_geo_gui.Gui(self.Radar_Panel)

        self.ideam_gui.Radar_Panel.out_down_folder_button.configure(
            command=lambda: Radar_functions_2.get_folderpath(self.Radar_Panel.out_donwload_folder_path))
        self.ideam_gui.Radar_Panel.avail_radar_button.configure(
            command=lambda: Radar_functions_2.get_radar_list(self.Radar_Panel))
        self.ideam_gui.Radar_Panel.save_nc_checkbox.configure(
            command=lambda: Radar_functions_2.interpolate_on_select(self.Radar_Panel))
        self.ideam_gui.Radar_Panel.save_tiff_checkbox.configure(
            command=lambda: Radar_functions_2.interpolate_on_select(self.Radar_Panel))
        self.ideam_gui.Radar_Panel.down_button.configure(
            command=lambda: Radar_functions_2.main_download(self.Radar_Panel))

        self.Radar_Panel.download_title.bind("<Button-1>", lambda event: Radar_functions_2.panel_expand(
            panel_name=self.Radar_Panel.download_ideam_content,
            row='1',
            up_arrow=self.Radar_Panel.ideam_up_arrow,
            down_arrow=self.Radar_Panel.ideam_down_arrow,
            state_var=self.Radar_Panel.dowload_ideam_frame_open))

        self.Radar_Panel.ref_to_pp_title.bind("<Button-1>", lambda event: Radar_functions_2.panel_expand(
            panel_name=self.Radar_Panel.ref_to_pp_content,
            row='1',
            up_arrow=self.Radar_Panel.ref_to_pp_up_arrow,
            down_arrow=self.Radar_Panel.ref_to_pp_down_arrow,
            state_var=self.Radar_Panel.ref_to_pp_frame_open))

        self.Radar_Panel.raw_to_nc_title.bind("<Button-1>", lambda event: Radar_functions_2.panel_expand(
            panel_name=self.Radar_Panel.raw_to_nc_content,
            row='1',
            up_arrow=self.Radar_Panel.raw_to_nc_up_arrow,
            down_arrow=self.Radar_Panel.raw_to_nc_down_arrow,
            state_var=self.Radar_Panel.raw_to_nc_frame_open))

        self.Radar_Panel.pol_to_geo_title.bind("<Button-1>", lambda event: Radar_functions_2.panel_expand(
            panel_name=self.Radar_Panel.pol_to_geo_content,
            row='1',
            up_arrow=self.Radar_Panel.pol_to_geo_up_arrow,
            down_arrow=self.Radar_Panel.pol_to_geo_down_arrow,
            state_var=self.Radar_Panel.pol_to_geo_frame_open))

        self.pol_to_geo_gui.Radar_Panel.in_polflat_folder_button.configure(
            command=lambda: Radar_functions_2.get_folderpath(self.Radar_Panel.in_polflat_folder_path))
        self.pol_to_geo_gui.Radar_Panel.polflat_main_button.configure(
            command=lambda: Radar_functions_2.convert_polar_to_geo_standalone(self.Radar_Panel))

        self.raw_to_nc_gui.Radar_Panel.in_raw_to_nc_folder_button.configure(
            command=lambda: Radar_functions_2.get_folderpath(self.Radar_Panel.in_raw_to_nc_folder_path))
        self.raw_to_nc_gui.Radar_Panel.out_raw_to_nc_folder_button.configure(
            command=lambda: Radar_functions_2.get_folderpath(self.Radar_Panel.out_raw_to_nc_folder_path))
        self.raw_to_nc_gui.Radar_Panel.nc_conversion_checkbox.configure(
            command=lambda: Radar_functions_2.nc_interpolate_unlock(self.Radar_Panel))
        self.raw_to_nc_gui.Radar_Panel.raw_to_nc_main_button.configure(
            command=lambda: Radar_functions_2.convert_to_nc_standalone(self.Radar_Panel))

        self.Radar_Panel.in_ref_to_pp_folder_path.trace(
            'w', lambda a, b, c: Radar_functions_2.unlock_nc_vars(self.Radar_Panel))
        self.ref_to_pp_gui.Radar_Panel.in_ref_to_pp_folder_button.configure(
            command=lambda: Radar_functions_2.get_folderpath(self.Radar_Panel.in_ref_to_pp_folder_path))
        self.ref_to_pp_gui.Radar_Panel.out_ref_to_pp_folder_button.configure(
            command=lambda: Radar_functions_2.get_folderpath(self.Radar_Panel.out_ref_to_pp_folder_path))
        self.ref_to_pp_gui.Radar_Panel.ref_to_pp_config_button.config(
            command=lambda: ref_to_pp_settings_window.open_settings_window(self.Radar_Panel))
        self.ref_to_pp_gui.Radar_Panel.ref_to_pp_main_button.configure(
            command=lambda: Radar_functions_2.run_ref_to_pp(self.Radar_Panel))

        self.ref_to_pp_gui.Radar_Panel.avail_radar_listbox.bind(
            '<<ListboxSelect>>', lambda event: Radar_functions_2.radar_onselect(self.Radar_Panel))

        self.Sat_Panel.main_button.configure(
            command=lambda: Satellite_Functions.run(self.Sat_Panel))
        self.Sat_Panel.mission.trace('w', miss_click)

    def start(self):
        self.root.mainloop()  # start monitoring and updating the GUI
