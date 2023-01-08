import tkinter as tk
import tkinter.ttk as ttk
import Satelite_GUI
import Radar_GUI
import Radar_functions_2
import Satellite_Functions
import ref_to_pp_settings_window

class MainWindow:
    def __init__(self,master=None):
        #Main notebook
        self.root = tk.Tk(master) #Makes the window
        self.root.wm_title("Rainraid V0.8") #Makes the title that will appear in the top left
        self.root.config(background = "#FFFFFF")
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
        #self.notebook.add(self.sat_frame, text='Satelite')



        # def ch_par_fr():
        #     Radar_functions.change_parameters_frame(self.RadarPanel)

        # def get_w_f_p():
        #     Radar_functions.get_working_folderpath(self.RadarPanel)

        # def get_m_p():
        #     Radar_functions.get_mask_filepath(self.RadarPanel)

        # def get_d_p():
        #     Radar_functions.get_data_folderpath(self.RadarPanel)

        # def disdro_click():
        #     Radar_functions.disdrometer_click(self.RadarPanel)

        def miss_click(*args):
            Satellite_Functions.mission_click(self.Sat_Panel)

        # def autotime_click():
        #     Radar_functions.autotime_click(self.RadarPanel)

        def get_f_path(text_variable):
            Radar_functions_2.get_folderpath(text_variable)

        def radar_list():
            Radar_functions_2.get_radar_list(self.Radar_Panel)

        def radar_unlock(evt):
            Radar_functions_2.radar_onselect(self.Radar_Panel)

        def interpolate_unlock():
            Radar_functions_2.interpolate_on_select(self.Radar_Panel)

        def ideam_download():
            Radar_functions_2.main_download(self.Radar_Panel)

        def unlock_nc_vars(*args):
            Radar_functions_2.unlock_nc_vars(self.Radar_Panel)

        def polar_conv_run():
            Radar_functions_2.conv_polartoflat(self.Radar_Panel)

        def raw_processing():
            Radar_functions_2.raw_to_nc(self.Radar_Panel)

        def settings_window():
            ref_to_pp_settings_window.open_settings_window(self.Radar_Panel)

        def radar_run():
            Radar_functions_2.run_ref_to_pp(self.Radar_Panel)

        def satellite_run():
            Satellite_Functions.run(self.Sat_Panel)

        # self.RadarPanel.polari_radio.configure(command=ch_par_fr)
        # self.RadarPanel.ZR_radio.configure(command=ch_par_fr)
        # self.RadarPanel.data_directory_button.configure(command=get_d_p)
        # self.RadarPanel.working_directory_button.configure(command=get_w_f_p)
        # self.RadarPanel.mask_directory_button.configure(command=get_m_p)
        # self.RadarPanel.disdrometer_radio.configure(command=disdro_click)
        # self.RadarPanel.auto_t_radio.configure(command=autotime_click)
        # self.RadarPanel.main_button.configure(command=radar_run)


        self.Radar_Panel.out_down_folder_button.configure(command= lambda: get_f_path(self.Radar_Panel.out_donwload_folder_path))
        self.Radar_Panel.avail_radar_button.configure(command=radar_list)
        self.Radar_Panel.save_nc_checkbox.configure(command=interpolate_unlock)
        self.Radar_Panel.save_tiff_checkbox.configure(command=interpolate_unlock)
        self.Radar_Panel.down_button.configure(command=ideam_download)



        # self.Radar_Panel2.in_polflat_folder_button.configure(command= lambda: get_f_path(self.Radar_Panel2.in_polflat_folder_path))
        # self.Radar_Panel2.out_polflat_folder_button.configure(command= lambda: get_f_path(self.Radar_Panel2.out_polflat_folder_path))
        # self.Radar_Panel2.polflat_main_button.configure(command = polar_conv_run)

        # self.Radar_Panel2.in_raw_to_nc_folder_button.configure(command=lambda: get_f_path(self.Radar_Panel2.in_raw_to_nc_folder_path))
        # self.Radar_Panel2.out_raw_to_nc_folder_button.configure(command=lambda: get_f_path(self.Radar_Panel2.out_raw_to_nc_folder_path))
        # self.Radar_Panel2.raw_to_nc_main_button.configure(command=raw_processing)

        self.Radar_Panel.in_ref_to_pp_folder_path.trace('w', unlock_nc_vars)
        self.Radar_Panel.in_ref_to_pp_folder_button.configure(command=lambda: get_f_path(self.Radar_Panel.in_ref_to_pp_folder_path))
        self.Radar_Panel.out_ref_to_pp_folder_button.configure(command=lambda: get_f_path(self.Radar_Panel.out_ref_to_pp_folder_path))
        # self.Radar_Panel2.out_ref_to_pp_mask_folder_button.configure(command=lambda: get_f_path(self.Radar_Panel2.ref_to_pp_mask_folder_path))
        self.Radar_Panel.ref_to_pp_config_button.config(command=settings_window)
        self.Radar_Panel.ref_to_pp_main_button.configure(command=radar_run)

        self.Radar_Panel.avail_radar_listbox.bind('<<ListboxSelect>>', radar_unlock)


        self.Sat_Panel.main_button.configure(command=satellite_run)
        self.Sat_Panel.mission.trace('w', miss_click)

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI