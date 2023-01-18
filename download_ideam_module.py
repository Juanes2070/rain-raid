import time
import download_ideam_gui
import out_textbox_write
import Radar_functions
import aws_tools
import tkinter as tk
import os
import shutil


class Module:
    def __init__(self, root, radar_frame, out_textbox):

        self.root = root
        self.gui = download_ideam_gui.Gui(root, radar_frame)
        self.gui.out_textbox = out_textbox

        self.gui.out_down_folder_button.configure(
            command=lambda: Radar_functions.get_folderpath(self.gui.out_download_folder_path))
        self.gui.avail_radar_button.configure(
            command=lambda: get_radar_list())
        self.gui.save_nc_checkbox.configure(
            command=lambda: interpolate_on_select())
        self.gui.save_tiff_checkbox.configure(
            command=lambda: interpolate_on_select())
        self.gui.down_button.configure(
            command=lambda: main_download())

        self.gui.download_title.bind("<Button-1>", lambda event: Radar_functions.panel_expand(
            panel_name=self.gui.download_ideam_content,
            row='1',
            up_arrow=self.gui.ideam_up_arrow,
            down_arrow=self.gui.ideam_down_arrow,
            state_var=self.gui.download_ideam_frame_open))

        self.gui.avail_radar_listbox.bind(
            '<<ListboxSelect>>', lambda event: radar_onselect())

        def get_radar_list():
            sta_date = self.gui.start_date_entry.get_date()
            end_date = self.gui.end_date_entry.get_date()
            aws_tools.radar_list(sta_date, end_date, self.gui)

        def radar_onselect():
            self.gui.selected_radar.set(self.gui.avail_radar_listbox.get(self.gui.avail_radar_listbox.curselection()))
            self.gui.save_raw_checkbox.configure(state='normal')
            self.gui.save_nc_checkbox.configure(state='normal')
            self.gui.save_tiff_checkbox.configure(state='normal')

        def interpolate_on_select():
            if self.gui.save_nc_var.get() or self.gui.save_tiff_var.get():
                self.gui.interp_options_select.configure(state='normal')
            else:
                self.gui.interp_options_select.configure(state='disabled')

        def download_raw():
            sta_date = self.gui.start_date_entry.get_date()
            end_date = self.gui.end_date_entry.get_date()
            out_folder = self.gui.out_download_folder_path.get()
            radar_name = self.gui.selected_radar.get()
            interval = int(self.gui.interval.get())

            out_raw_folder = out_folder + "RAW/"
            os.mkdir(out_raw_folder)

            aws_tools.aws_radar_download(start_date=sta_date,
                                         end_date=end_date,
                                         radar_name=radar_name,
                                         interval=interval,
                                         out_folder=out_raw_folder,
                                         gui=self.gui)

            out_str = "Archivos guardados correctamente en: \n" + out_folder + '\n'
            out_textbox_write.write(self.gui.out_textbox, out_str)
            return out_raw_folder

        def main_download():

            radar_name = self.gui.selected_radar.get()
            sta_date = self.gui.start_date_entry.get_date()
            end_date = self.gui.end_date_entry.get_date()
            out_folder = self.gui.out_download_folder_path.get()
            save_raw = self.gui.save_raw_var.get()
            save_nc = self.gui.save_nc_var.get()
            save_tiff = self.gui.save_tiff_var.get()
            interpolate = self.gui.interp_options.get()
            interval = self.gui.interval.get()
            nc_project = True

            if save_raw is False and save_nc is False and save_tiff is False:
                out_textbox.insert(tk.END, "Seleccionar archivos a guardar")
                self.gui.root.update()
                return

            current_time = time.strftime("%H:%M:%S", time.localtime())
            start_time = time.perf_counter()

            summary_list = [current_time,
                            'Radar seleccionado: ' + radar_name,
                            'Fecha inicial: ' + str(sta_date),
                            'Fecha final: ' + str(end_date),
                            'Intervalo (min): ' + interval,
                            'Formatos seleccionados: ']

            if save_raw is True:
                summary_list.append('RAW')
            if save_nc is True:
                summary_list.append('netCDF4')
            if save_tiff is True:
                summary_list.append('Tiff')
            if interpolate != 'No interpolar':
                summary_list.append('Interpolación: ' + interpolate)
            summary_list.append('Guardar en: ' + out_folder)
            summary = str()
            for line in summary_list:
                summary = summary + line + '\n'

            out_textbox_write.write(textbox=self.gui.out_textbox,
                                    text=summary,
                                    delete_prev=True)
            self.gui.root.update()

            try:
                shutil.rmtree(out_folder)
            except PermissionError:
                error_str = 'Error: \nLa carpeta destino debe estar vacía'
                out_textbox_write.write(self.gui.out_textbox, error_str)
                return
            except FileNotFoundError:
                error_str = 'Error: \nRuta no encontrada, intente otra carpeta'
                out_textbox_write.write(self.gui.out_textbox, error_str)
                return
            else:
                os.mkdir(out_folder)
                nc_folder = out_folder + 'netCDF4/'
                tiff_folder = out_folder + 'Tiff/'
                os.mkdir(nc_folder)
                os.mkdir(tiff_folder)

            if save_raw is True and save_nc is False and save_tiff is False:
                download_raw()
                shutil.rmtree(nc_folder)
                shutil.rmtree(tiff_folder)

            if save_raw is True and save_nc is True and save_tiff is False:
                raw_folder = download_raw()
                Radar_functions.convert_to_nc(self.gui, raw_folder, nc_folder, interpolate, nc_project)
                shutil.rmtree(tiff_folder)

            if save_raw is True and save_nc is True and save_tiff is True:
                raw_folder = download_raw()
                Radar_functions.convert_to_nc(self.gui, raw_folder, nc_folder, interpolate, nc_project)
                Radar_functions.convert_to_tiff(self.gui, nc_folder, tiff_folder)

            if save_raw is False and save_nc is True and save_tiff is False:
                raw_folder = download_raw()
                Radar_functions.convert_to_nc(self.gui, raw_folder, nc_folder, interpolate, nc_project)
                shutil.rmtree(raw_folder)
                shutil.rmtree(tiff_folder)

            if save_raw is False and save_nc is True and save_tiff is True:
                raw_folder = download_raw()
                Radar_functions.convert_to_nc(self.gui, raw_folder, nc_folder, interpolate, nc_project)
                Radar_functions.convert_to_tiff(self.gui, nc_folder, tiff_folder)

                shutil.rmtree(raw_folder)

            if save_raw is False and save_nc is False and save_tiff is True:
                raw_folder = download_raw()
                Radar_functions.convert_to_nc(self.gui, raw_folder, nc_folder, interpolate, nc_project)
                Radar_functions.convert_to_tiff(self.gui, nc_folder, tiff_folder)

                shutil.rmtree(raw_folder)
                shutil.rmtree(nc_folder)

            if save_raw is True and save_nc is False and save_tiff is True:
                download_raw()
                Radar_functions.convert_to_nc(self.gui, raw_folder, nc_folder, interpolate, nc_project)
                Radar_functions.convert_to_tiff(self.gui, nc_folder, tiff_folder)
                shutil.rmtree(nc_folder)

            end_time = time.perf_counter()
            time_of_exec = end_time - start_time
            out_textbox_write.write(self.gui.out_textbox, 'Tiempo de ejecución: {:.2f} s\n'.format(time_of_exec))

            self.gui.root.update()
