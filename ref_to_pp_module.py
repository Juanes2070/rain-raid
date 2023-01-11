import ref_to_pp_gui
import Radar_functions
import os
import ref_to_pp_settings_window
import tkinter as tk
import ref_to_pp
import shutil
from get_nc_variables import get_nc_variables
from multiprocessing import Pool
from itertools import repeat


class Module:
    def __init__(self, root, radar_frame, out_textbox):

        self.root = root
        self.gui = ref_to_pp_gui.Gui(root, radar_frame)
        self.gui.out_textbox = out_textbox

        self.gui.ref_to_pp_title.bind("<Button-1>", lambda event: Radar_functions.panel_expand(
            panel_name=self.gui.ref_to_pp_content,
            row='1',
            up_arrow=self.gui.ref_to_pp_up_arrow,
            down_arrow=self.gui.ref_to_pp_down_arrow,
            state_var=self.gui.ref_to_pp_frame_open))

        self.gui.in_ref_to_pp_folder_path.trace(
            'w', lambda a, b, c: unlock_nc_vars())
        self.gui.in_ref_to_pp_folder_button.configure(
            command=lambda: Radar_functions.get_folderpath(self.gui.in_ref_to_pp_folder_path))
        self.gui.out_ref_to_pp_folder_button.configure(
            command=lambda: Radar_functions.get_folderpath(self.gui.out_ref_to_pp_folder_path))
        self.gui.ref_to_pp_config_button.config(
            command=lambda: ref_to_pp_settings_window.open_settings_window(self.gui))
        self.gui.ref_to_pp_main_button.configure(
            command=lambda: run_ref_to_pp())

        def unlock_nc_vars():
            file_route = self.gui.in_ref_to_pp_folder_path.get()
            file = os.listdir(file_route)[0]
            nc_vars = get_nc_variables(file_route + file)

            if nc_vars:

                self.gui.ref_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.ref_var.set(nc_vars[4])
                self.gui.lat_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.lat_var.set(nc_vars[1])
                self.gui.lon_var_combo.configure(state='enabled', values=nc_vars)
                self.gui.lon_var.set(nc_vars[2])
                self.gui.ref_to_pp_main_button.configure(state='enabled')

            else:
                self.gui.ref_var.set("Seleccionar carpeta de nc")
                self.gui.lat_var.set("Seleccionar carpeta de nc")
                self.gui.lon_var.set("Seleccionar carpeta de nc")

                self.gui.ref_var_combo.configure(state='disabled')
                self.gui.lat_var_combo.configure(state='disabled')
                self.gui.lon_var_combo.configure(state='disabled')

        def run_ref_to_pp():
            # TODO programar interpolacion
            self.gui.out_textbox.configure(state='normal')
            self.gui.out_textbox.delete('1.0', tk.END)
            self.gui.out_textbox.insert(tk.END, "Comenzando ejecución...\n")
            self.gui.root.update()

            in_folder = self.gui.in_ref_to_pp_folder_path.get()
            out_folder = self.gui.out_ref_to_pp_folder_path.get()

            try:
                shutil.rmtree(out_folder)
                os.mkdir(out_folder)
            except:
                pass

            files = os.listdir(in_folder)
            file_paths = []
            for file in files:
                file_paths.append(in_folder + file)

            self.gui.out_textbox.insert(tk.END, str(len(files)) + " Archivos encontrados\n")
            self.gui.out_textbox.insert(tk.END, "Procesando... \n")
            self.gui.root.update()

            ref_var = self.gui.ref_var.get()
            lat_var = self.gui.lat_var.get()
            lon_var = self.gui.lon_var.get()

            a_zr = float(self.gui.a_zr_var.get())
            b_zr = float(self.gui.b_zr_var.get())
            m_disd = float(self.gui.m_disd_var.get())
            b_disd = float(self.gui.b_disd_var.get())
            trunc = float(self.gui.trunc_var.get())

            arguments = zip(file_paths,
                            repeat(ref_var),
                            repeat(lat_var),
                            repeat(lon_var),
                            repeat(m_disd),
                            repeat(b_disd),
                            repeat(b_zr),
                            repeat(a_zr),
                            repeat(trunc),
                            repeat(out_folder))

            with Pool() as p:
                p.starmap(ref_to_pp.nc_file_processing, arguments)

            self.gui.out_textbox.insert(tk.END, "Archivos guardados correctamente en: \n")
            self.gui.out_textbox.insert(tk.END, out_folder)
            self.gui.out_textbox.configure(state='disabled')
            self.gui.root.update()




