from tkinter import filedialog as filed
import tkinter as tk
import datetime
import os
import shutil
import pyart_tools
import aws_tools
import polar_to_geo
import ref_to_pp
from get_nc_variables import get_nc_variables
from multiprocessing import Pool
from itertools import repeat

#TODO agregar timestamps al out
#TODO agregar summary de ejecución al out
#TODO agregar scrollbar al out


def get_folderpath(text_vaiable):
    folder_selected = filed.askdirectory()
    text_vaiable.set(folder_selected+"/")

def get_radar_list(self):
    sta_date = self.start_date_entry.get_date()
    end_date = self.end_date_entry.get_date()
    aws_tools.radar_list(sta_date,end_date,self)

def radar_onselect(self):
    self.selected_radar.set(self.avail_radar_listbox.get(self.avail_radar_listbox.curselection()))
    self.save_raw_checkbox.configure(state='normal')
    self.save_nc_checkbox.configure(state='normal')
    self.save_tiff_checkbox.configure(state='normal')

def interpolate_on_select(self):
    if self.save_nc_var.get() == True or self.save_tiff_var.get():
        self.interp_options_select.configure(state='normal')
    else:
        self.interp_options_select.configure(state='disabled')

def download_raw(self):
    sta_date = self.start_date_entry.get_date()
    end_date = self.end_date_entry.get_date()
    out_folder = self.out_donwload_folder_path.get()
    radar_name = self.selected_radar.get()
    interval = int(self.interval.get())

    out_raw_folder = out_folder + "RAW/"
    os.mkdir(out_raw_folder)

    aws_tools.aws_radar_download(start_date=sta_date,
                                 end_date=end_date,
                                 radar_name=radar_name,
                                 interval=interval,
                                 out_folder=out_raw_folder,
                                 gui=self)
    return out_raw_folder

def convert_to_nc(self,in_raw_folder):

    self.out_textbox.insert(tk.END, "Convirtiendo archivos a netCDF4... \n")
    self.root.update()

    out_folder = self.out_donwload_folder_path.get()
    out_nc_folder = out_folder + "netCDF/"
    os.mkdir(out_nc_folder)
    days = os.listdir(in_raw_folder)
    interpolate = self.interp_options.get()
    for day in days:
        files = os.listdir(in_raw_folder + day + "/")
        file_list = []
        for file in files:
            file_list.append(in_raw_folder + day + "/" + file)

        with Pool() as p:
            p.starmap(pyart_tools.raw_to_netcdf, zip(file_list, repeat(out_nc_folder),repeat(interpolate)))

        self.out_textbox.insert(tk.END, "Coversión finalizada \n")
        self.root.update()
    return out_nc_folder

def convert_to_tiff(self,in_nc_folder):

    self.out_textbox.insert(tk.END, "Convirtiendo archivos a Tiff... \n")
    self.root.update()

    out_folder = self.out_donwload_folder_path.get()
    out_tiff_folder = out_folder + "Tiff/"
    os.mkdir(out_tiff_folder)
    files = []
    with os.scandir(in_nc_folder) as entries:
        for entry in entries:
            files.append(entry.path)

    with Pool() as p:
        p.starmap(polar_to_geo.grid_to_tif, zip(files, repeat(out_tiff_folder)))

    self.out_textbox.insert(tk.END, "Coversión finalizada \n")
    self.root.update()

def main_download(self):
    self.out_textbox.configure(state='normal')
    self.out_textbox.delete('1.0',tk.END)
    self.root.update()

    #TODO Handle folder exception
    out_folder = self.out_donwload_folder_path.get()

    save_raw = self.save_raw_var.get()
    save_nc = self.save_nc_var.get()
    save_tiff = self.save_tiff_var.get()

    if save_raw == False and save_nc == False and save_tiff == False:
        self.out_textbox.insert(tk.END, "Seleccionar archivos a guardar")
        self.root.update()
        return

    try:
        shutil.rmtree(out_folder)
        os.mkdir(out_folder)
    except:
        pass

    if save_raw == True and save_nc == False and save_tiff == False:
        download_raw(self)

    if save_raw == True and save_nc == True and save_tiff == False:
        raw_folder = download_raw(self)
        convert_to_nc(self,raw_folder)

    if save_raw == True and save_nc == True and save_tiff == True:
        raw_folder = download_raw(self)
        nc_folder = convert_to_nc(self, raw_folder)
        convert_to_tiff(self,nc_folder)

    if save_raw == False and save_nc == True and save_tiff == False:
        raw_folder = download_raw(self)
        convert_to_nc(self, raw_folder)
        shutil.rmtree(raw_folder)

    if save_raw == False and save_nc == True and save_tiff == True:
        raw_folder = download_raw(self)
        nc_folder= convert_to_nc(self, raw_folder)
        convert_to_tiff(self,nc_folder)

        shutil.rmtree(raw_folder)

    if save_raw == False and save_nc == False and save_tiff == True:
        raw_folder = download_raw(self)
        nc_folder = convert_to_nc(self, raw_folder)
        convert_to_tiff(self,nc_folder)

        shutil.rmtree(raw_folder)
        shutil.rmtree(nc_folder)

    self.out_textbox.insert(tk.END, "Archivos guardados correctamente en: \n")
    self.out_textbox.insert(tk.END, out_folder)
    self.out_textbox.configure(state='disabled')
    self.root.update()

def unlock_nc_vars(self):

    file_route = self.in_ref_to_pp_folder_path.get()
    file = os.listdir(file_route)[0]
    vars = get_nc_variables(file_route+file)

    if vars == False:
        self.ref_var.set("Seleccionar carpeta de nc")
        self.lat_var.set("Seleccionar carpeta de nc")
        self.lon_var.set("Seleccionar carpeta de nc")

        self.ref_var_combo.configure(state='disabled')
        self.lat_var_combo.configure(state='disabled')
        self.lon_var_combo.configure(state='disabled')

    else:

        self.ref_var_combo.configure(state ='enabled', values = vars)
        self.ref_var.set(vars[4])
        self.lat_var_combo.configure(state='enabled', values=vars)
        self.lat_var.set(vars[1])
        self.lon_var_combo.configure(state='enabled', values=vars)
        self.lon_var.set(vars[2])
        self.ref_to_pp_main_button.configure(state='enabled')


def run_ref_to_pp(self):

    #TODO programar interpolacion
    self.out_textbox.configure(state='normal')
    self.out_textbox.delete('1.0', tk.END)
    self.out_textbox.insert(tk.END, "Comenzando ejecución...\n")
    self.root.update()

    in_folder = self.in_ref_to_pp_folder_path.get()
    out_folder = self.out_ref_to_pp_folder_path.get()

    try:
        shutil.rmtree(out_folder)
        os.mkdir(out_folder)
    except:
        pass

    files = os.listdir(in_folder)
    file_paths = []
    for file in files:
        file_paths.append(in_folder+file)

    self.out_textbox.insert(tk.END, str(len(file)) + " Archivos encontrados\n")
    self.out_textbox.insert(tk.END, "Procesando... \n")
    self.root.update()

    ref_var = self.ref_var.get()
    lat_var = self.lat_var.get()
    lon_var = self.lon_var.get()

    a_zr = float(self.a_zr_var.get())
    b_zr = float(self.b_zr_var.get())
    m_disd = float(self.m_disd_var.get())
    b_disd = float(self.b_disd_var.get())
    trunc = float(self.trunc_var.get())


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
        p.starmap(ref_to_pp.nc_file_processing,arguments)

    self.out_textbox.insert(tk.END, "Archivos guardados correctamente en: \n")
    self.out_textbox.insert(tk.END, out_folder)
    self.out_textbox.configure(state='disabled')
    self.root.update()


    #start_time = datetime.datetime.now()


