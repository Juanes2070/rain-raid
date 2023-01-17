import download_satellite_gui
import login_sat_gui
import out_textbox_write
import shutil
import os
from imerg_download import main_imerg
from chirps_request import chirps_download

import Radar_functions


class Module:
    def __init__(self, root, satellite_frame, out_textbox):

        self.root = root
        self.gui = download_satellite_gui.Gui(root, satellite_frame)
        self.gui.out_textbox = out_textbox

        self.gui.mission.trace('w', lambda *args: mission_click())
        self.gui.logged_in.trace('w', lambda *args: check_login())
        self.gui.main_button.configure(command=lambda: run())

        Radar_functions.panel_expand(
            panel_name=self.gui.download_satellite_content,
            row=1,
            up_arrow=self.gui.satellite_up_arrow,
            down_arrow=self.gui.satellite_down_arrow,
            state_var=self.gui.download_satellite_frame_open
        )

        self.gui.download_title.bind("<Button-1>", lambda event: Radar_functions.panel_expand(
            panel_name=self.gui.download_satellite_content,
            row=1,
            up_arrow=self.gui.satellite_up_arrow,
            down_arrow=self.gui.satellite_down_arrow,
            state_var=self.gui.download_satellite_frame_open
        ))

        self.gui.out_folder_button.configure(
            command=lambda: Radar_functions.get_folderpath(self.gui.out_folder_path))

        self.gui.login_button.configure(command=lambda: change_login_credentials())

        def change_login_credentials():
            login_window = login_sat_gui.Window(self.root,
                                                self.gui)
            login_window.login_button.configure(command=lambda: login_window.check_login())

        def run():

            sta_date = self.gui.start_date_entry.get_date()
            end_date = self.gui.end_date_entry.get_date()
            mission = self.gui.mission.get()
            out_folder = self.gui.out_folder_path.get()
            try:
                shutil.rmtree(out_folder)
            except PermissionError:
                error_str = 'Error: \nLa carpeta destino debe estar vacía'
                out_textbox_write.write(self.gui.out_textbox, error_str, True)
                return
            else:
                os.mkdir(out_folder)
            if mission == 'GPM_3IMERGHH':
                if self.gui.logged_in.get():
                    main_imerg(start_date=sta_date,
                               end_date=end_date,
                               out_folder=out_folder,
                               user=self.gui.username_var.get(),
                               psswrd=self.gui.password_var.get(),
                               gui=self.gui)

            if mission == 'CHIRPS-2.0':
                chirps_download(start_date=sta_date,
                                end_date=end_date,
                                out_folder=out_folder,
                                gui=self.gui)

        def mission_click():
            mission = self.gui.mission.get()
            if mission == 'CHIRPS-2.0':
                self.gui.login_button.configure(state='disabled')
                self.gui.login_button.configure(state='disabled')
                out_textbox_write.write(self.gui.out_textbox, '', True)
            elif mission == 'GPM_3IMERGHH':
                check_login()
                self.gui.login_button.configure(state='enabled')
                self.gui.login_button.configure(state='enabled')
            self.gui.root.update()

        def check_login():
            if self.gui.logged_in.get():
                out_textbox_write.write(self.gui.out_textbox, 'Sesion Iniciada Correctamente', True)
            else:
                out_textbox_write.write(self.gui.out_textbox, 'Por favor inicie sesión en EarthData', True)
            self.root.update()
        #TODO change this to false
        self.gui.logged_in.set(True)
