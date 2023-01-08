import tkinter as tk
from imerg_download import main_imerg
from chirps_request import chirps_download
import datetime

def run(self):
    sta_date = self.start_date.get()
    sta_date = datetime.datetime.strptime(sta_date, "%d/%m/%Y")
    end_date = self.end_date.get()
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")

    self.out_text.insert('0.0', "Comenzando ejecución...\n")
    self.root.update()

    if self.mission.get() == 'IMERG':
        main_imerg(start_date=sta_date,
                   end_date=end_date,
                   out_folder=self.out_folder_path.get(),
                   user=self.username.get(),
                   psswrd=self.password.get(),
                   gui=self)


    if self.mission.get() == 'CHIRPS':
        chirps_download(start_date=sta_date,
                        end_date=end_date,
                        out_folder=self.out_folder_path.get(),
                        gui=self)


def mission_click(self):
    if self.mission.get() == 'CHIRPS':
        self.username_entry.configure(state='disabled')
        self.password_entry.configure(state='disabled')
    elif self.mission.get() == 'IMERG':
        self.username_entry.configure(state='enabled')
        self.password_entry.configure(state='enabled')
    self.root.update()

