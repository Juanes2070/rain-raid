import download_satellite_gui
import login_sat_gui
from imerg_download import main_imerg
from chirps_request import chirps_download

import Radar_functions


class Module:
    def __init__(self, root, satellite_frame, out_textbox):

        self.root = root
        self.gui = download_satellite_gui.Gui(root, satellite_frame)
        self.gui.out_textbox = out_textbox


        self.gui.mission.trace('w', lambda *args: mission_click())
        self.gui.main_button.configure(command=lambda: run())

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
                                 satellite_frame,
                                 self.gui.username,
                                 self.gui.password)
            login_window.login_button.configure(command=lambda: login_window.check_login())

        def run():

            sta_date = self.gui.start_date_entry.get_date()
            end_date = self.gui.end_date_entry.get_date()
            mission = self.gui.mission.get()

            # self.gui.out_textbox.configure(state='normal')
            #
            # self.root.update()

            if mission == 'IMERG':
                main_imerg(start_date=sta_date,
                           end_date=end_date,
                           out_folder=self.gui.out_folder_path.get(),
                           user=self.gui.username.get(),
                           psswrd=self.gui.password.get(),
                           gui=self.gui)

            if mission == 'CHIRPS':
                chirps_download(start_date=sta_date,
                                end_date=end_date,
                                out_folder=self.gui.out_folder_path.get(),
                                gui=self.gui)

        def mission_click():
            mission = self.gui.mission.get()
            if mission == 'CHIRPS':
                self.gui.login_button.configure(state='disabled')
                self.gui.login_button.configure(state='disabled')
            elif mission == 'IMERG':
                self.gui.login_button.configure(state='enabled')
                self.gui.login_button.configure(state='enabled')
            self.gui.root.update()
