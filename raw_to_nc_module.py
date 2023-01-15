import out_textbox_write
import raw_to_nc_gui
import Radar_functions
import os
import shutil
import tkinter as tk


class Module:
    def __init__(self, root, radar_frame, out_textbox):

        self.root = root
        self.gui = raw_to_nc_gui.Gui(root, radar_frame)
        self.gui.out_textbox = out_textbox

        self.gui.raw_to_nc_title.bind("<Button-1>", lambda event: Radar_functions.panel_expand(
            panel_name=self.gui.raw_to_nc_content,
            row='1',
            up_arrow=self.gui.raw_to_nc_up_arrow,
            down_arrow=self.gui.raw_to_nc_down_arrow,
            state_var=self.gui.raw_to_nc_frame_open))

        self.gui.in_raw_to_nc_folder_button.configure(
            command=lambda: Radar_functions.get_folderpath(self.gui.in_raw_to_nc_folder_path))
        self.gui.out_raw_to_nc_folder_button.configure(
            command=lambda: Radar_functions.get_folderpath(self.gui.out_raw_to_nc_folder_path))
        self.gui.nc_conversion_checkbox.configure(
            command=lambda: nc_interpolate_unlock())
        self.gui.raw_to_nc_main_button.configure(
            command=lambda: convert_to_nc_standalone())

        def nc_interpolate_unlock():
            if self.gui.raw_to_nc_conversion.get():
                self.gui.nc_interp_options_select.configure(state='normal')
            else:
                self.gui.nc_interp_options_select.configure(state='disabled')

        def convert_to_nc_standalone():
            out_textbox_write.write(self.gui.out_textbox,'',True)
            in_folder = self.gui.in_raw_to_nc_folder_path.get()
            out_folder = self.gui.out_raw_to_nc_folder_path.get()
            interpolate = self.gui.raw_to_nc_interpolate.get()
            project = self.gui.raw_to_nc_conversion.get()

            try:
                shutil.rmtree(out_folder)
                os.mkdir(out_folder)
            except PermissionError:
                pass

            Radar_functions.convert_to_nc(self.gui, in_folder, out_folder, interpolate, project)
