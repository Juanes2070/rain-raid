from tkinter import filedialog as filed
import tkinter as tk
import datetime
import os
import pyart_tools
import polar_to_geo
from multiprocessing import Pool
from itertools import repeat

#TODO agregar timestamps al out
#TODO agregar summary de ejecución al out
#TODO agregar scrollbar al out


def get_folderpath(text_vaiable):
    folder_selected = filed.askdirectory()
    text_vaiable.set(folder_selected+"/")

def panel_expand(panel_name, row, up_arrow, down_arrow, state_var):
    if state_var.get() == False:
        panel_name.grid(column='0', row=row, sticky='nsew')
        down_arrow.grid_forget()
        up_arrow.grid(row='0',column='1')
        state_var.set(True)
    else:
        panel_name.grid_forget()
        up_arrow.grid_forget()
        down_arrow.grid(row='0', column='1')
        state_var.set(False)

def convert_to_nc(radar_gui,in_raw_folder,out_folder,interpolate,project):

    radar_gui.out_textbox.insert(tk.END, "Convirtiendo archivos a netCDF4... \n")
    radar_gui.root.update()

    folder_list = []
    file_path_lists = []
    for root, dirs, files in os.walk(in_raw_folder):
        file_paths = [os.path.join(root, file) for file in files]
        file_path_lists.append(file_paths)

        for folder in dirs:
            folder_route = os.path.join(out_folder,folder+'/')
            os.mkdir(folder_route)
            folder_list.append(folder_route)

    if len(folder_list) == 0:
        folder_list.append(out_folder+'/')
    else:
        file_path_lists.pop(0)

    for i, out_folder in enumerate(folder_list):
        with Pool() as p:
            p.starmap(pyart_tools.raw_to_netcdf, zip(file_path_lists[i],
                                                     repeat(out_folder),
                                                     repeat(interpolate),
                                                     repeat(project)))

    radar_gui.out_textbox.insert(tk.END, "Coversión finalizada \n")
    radar_gui.root.update()

#TODO agregar opcion de elegir variables en los netcdf

def convert_to_tiff(radar_gui, in_nc_folder, out_folder):

    radar_gui.out_textbox.insert(tk.END, "Convirtiendo archivos a Tiff... \n")
    radar_gui.root.update()

    folder_list = []
    file_path_lists = []
    for root, dirs, files in os.walk(in_nc_folder):
        file_paths = [os.path.join(root, file) for file in files]
        file_path_lists.append(file_paths)

        for folder in dirs:
            folder_route = os.path.join(out_folder,folder+'/')
            os.mkdir(folder_route)
            folder_list.append(folder_route)

    if len(folder_list) == 0:
        folder_list.append(out_folder+'/')
    else:
        file_path_lists.pop(0)

    for i, out_folder in enumerate(folder_list):
        with Pool() as p:
            p.starmap(polar_to_geo.grid_to_tif, zip(file_path_lists[i], repeat(out_folder)))



    radar_gui.out_textbox.insert(tk.END, "Coversión finalizada \n")
    radar_gui.root.update()

    #start_time = datetime.datetime.now()



