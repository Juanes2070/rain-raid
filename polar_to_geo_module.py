import polar_to_geo_gui
import Radar_functions
import polar_to_geo
import tkinter as tk
import os
import out_textbox_write
from multiprocessing import Pool
from get_nc_variables import get_nc_variables
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
        self.gui.in_polflat_folder_path.trace(
            'w', lambda a, b, c: unlock_nc_vars())
        self.gui.polflat_main_button.configure(
            command=lambda: convert_polar_to_geo_standalone())

        def unlock_nc_vars():
            file_route = self.gui.in_polflat_folder_path.get()
            try:
                file = os.listdir(file_route)[0]
                nc_vars = get_nc_variables(file_route + file)
            except FileNotFoundError:
                return
            # TODO autodectar variables
            if nc_vars:

                self.gui.ref_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.ref_var.set(nc_vars[4])
                self.gui.lat_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.lat_var.set(nc_vars[26])
                self.gui.lon_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.lon_var.set(nc_vars[27])
                self.gui.dist_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.azim_var.set(nc_vars[2])
                self.gui.azim_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.dist_var.set(nc_vars[1])
                self.gui.polflat_main_button.configure(state='enabled')

            else:
                self.gui.ref_var.set("Seleccionar carpeta de nc")
                self.gui.lat_var.set("Seleccionar carpeta de nc")
                self.gui.lon_var.set("Seleccionar carpeta de nc")
                self.gui.dist_var.set("Seleccionar carpeta de nc")
                self.gui.azim_var.set("Seleccionar carpeta de nc")

                self.gui.azim_var_combo.configure(state='disabled')
                self.gui.dist_var_combo.configure(state='disabled')
                self.gui.ref_var_combo.configure(state='disabled')
                self.gui.lat_var_combo.configure(state='disabled')
                self.gui.lon_var_combo.configure(state='disabled')

                self.gui.polflat_main_button.configure(state='disabled')

        def convert_polar_to_geo_standalone():
            start_str = "Agregando variables convertidas a\narchivos netCDF4... \n"
            out_textbox_write.write(self.gui.out_textbox, start_str, True)
            self.gui.root.update()

            in_folder = self.gui.in_polflat_folder_path.get()
            interpolate = self.gui.pol_to_geo_interpolate.get()
            distance = self.gui.dist_var.get()
            azimuth = self.gui.azim_var.get()
            reflectivity = self.gui.ref_var.get()
            latitude = self.gui.lat_var.get()
            longitude = self.gui.lon_var.get()

            Radar_functions.convert_polar_to_geo(in_folder=in_folder,
                                                 interpolate=interpolate,
                                                 distance=distance,
                                                 azim=azimuth,
                                                 ref=reflectivity,
                                                 lat=latitude,
                                                 lon=longitude)

            out_textbox_write.write(self.gui.out_textbox, "Proceso finalizado \n")
            self.gui.root.update()
