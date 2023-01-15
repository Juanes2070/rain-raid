from tkinter import filedialog as filed
import out_textbox_write
import os
import pyart_tools
import polar_to_geo
from multiprocessing import Pool
from itertools import repeat


def get_folderpath(text_vaiable):
    folder_selected = filed.askdirectory()
    text_vaiable.set(folder_selected + "/")


def panel_expand(panel_name, row, up_arrow, down_arrow, state_var):
    if state_var.get() == False:
        panel_name.grid(column='0', row=row, sticky='nsew')
        down_arrow.grid_forget()
        up_arrow.grid(row='0', column='1')
        state_var.set(True)
    else:
        panel_name.grid_forget()
        up_arrow.grid_forget()
        down_arrow.grid(row='0', column='1')
        state_var.set(False)


def convert_to_nc(radar_gui, in_raw_folder, out_folder, interpolate, project):
    out_textbox_write.write(radar_gui.out_textbox, "Convirtiendo archivos a netCDF4... \n")
    radar_gui.root.update()

    folder_list = []
    file_path_lists = []
    for root, dirs, files in os.walk(in_raw_folder):
        file_paths = [os.path.join(root, file) for file in files]
        file_path_lists.append(file_paths)

        for folder in dirs:
            folder_route = os.path.join(out_folder, folder + '/')
            os.mkdir(folder_route)
            folder_list.append(folder_route)

    if len(folder_list) == 0:
        folder_list.append(out_folder + '/')
    else:
        file_path_lists.pop(0)

    for i, out_day_folder in enumerate(folder_list):
        with Pool() as p:
            p.starmap(pyart_tools.raw_to_netcdf, zip(file_path_lists[i],
                                                     repeat(out_day_folder),
                                                     repeat(interpolate)))
        if project:
            convert_polar_to_geo(in_folder=out_day_folder,
                                 interpolate=interpolate,
                                 distance='range',
                                 azim='azimuth',
                                 ref='reflectivity',
                                 lat='latitude',
                                 lon='longitude')

    out_textbox_write.write(radar_gui.out_textbox, "Coversión finalizada \n")
    out_textbox_write.write(radar_gui.out_textbox, "Archivos guardados correctamente en: \n" + out_folder)
    radar_gui.root.update()


def convert_polar_to_geo(in_folder, interpolate, distance, azim, ref, lat, lon):
    file_path_lists = []
    for root, dirs, files in os.walk(in_folder):
        file_paths = [os.path.join(root, file) for file in files]
        file_path_lists.append(file_paths)

    for i in range(len(file_path_lists)):
        with Pool() as p:
            arguments = zip(file_path_lists[i],
                            repeat(interpolate),
                            repeat(ref),
                            repeat(azim),
                            repeat(distance),
                            repeat(lat),
                            repeat(lon))
            p.starmap(polar_to_geo.antenna_to_grid, arguments)


def convert_to_tiff(radar_gui, in_nc_folder, out_folder):
    out_textbox_write.write(radar_gui.out_textbox, "Convirtiendo archivos a Tiff... \n")
    radar_gui.root.update()

    folder_list = []
    file_path_lists = []
    for root, dirs, files in os.walk(in_nc_folder):
        file_paths = [os.path.join(root, file) for file in files]
        file_path_lists.append(file_paths)

        for folder in dirs:
            folder_route = os.path.join(out_folder, folder + '/')
            os.mkdir(folder_route)
            folder_list.append(folder_route)

    if len(folder_list) == 0:
        folder_list.append(out_folder + '/')
    else:
        file_path_lists.pop(0)

    for i, out_folder in enumerate(folder_list):
        with Pool() as p:
            p.starmap(polar_to_geo.grid_to_tif, zip(file_path_lists[i], repeat(out_folder)))

    out_textbox_write.write(radar_gui.out_textbox, "Coversión finalizada \n")
    radar_gui.root.update()
