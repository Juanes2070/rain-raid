import polar_to_geo_gui
import Radar_functions
import polar_to_geo
import tkinter as tk
import os
from multiprocessing import Pool
from itertools import repeat


class Module:
    def __init__(self, root, radar_frame, out_textbox):

        self.root = root
        self.gui = polar_to_geo_gui.Gui(root, radar_frame)
        self.gui.out_textbox = out_textbox

        self.gui.pol_to_geo_title.bind("<Button-1>", lambda event: Radar_functions.panel_expand(
            panel_name=self.gui.pol_to_geo_content,
            row='1',
            up_arrow=self.gui.pol_to_geo_up_arrow,
            down_arrow=self.gui.pol_to_geo_down_arrow,
            state_var=self.gui.pol_to_geo_frame_open))

        self.gui.in_polflat_folder_button.configure(
            command=lambda: Radar_functions.get_folderpath(self.gui.in_polflat_folder_path))
        self.gui.polflat_main_button.configure(
            command=lambda: convert_polar_to_geo_standalone())

        def convert_polar_to_geo_standalone():

            self.gui.out_textbox.configure(state='normal')
            self.gui.out_textbox.delete('1.0', tk.END)
            self.gui.root.update()

            self.gui.out_textbox.insert(tk.END, "Agregando variables convertidas a \n")
            self.gui.out_textbox.insert(tk.END, "archivos netCDF4... \n")
            self.gui.root.update()

            in_folder = self.gui.in_polflat_folder_path.get()
            interpolate = self.gui.pol_to_geo_interpolate.get()
            file_path_lists = []

            for root, dirs, files in os.walk(in_folder):
                file_paths = [os.path.join(root, file) for file in files]
                file_path_lists.append(file_paths)

            for i in range(len(file_path_lists)):
                with Pool() as p:
                    p.starmap(polar_to_geo.antenna_to_grid, zip(file_path_lists[i], repeat(interpolate)))

            self.gui.out_textbox.insert(tk.END, "Proceso finalizado \n")
            self.gui.out_textbox.configure(state='disabled')
            self.gui.root.update()
