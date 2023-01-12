import requests
import datetime
import netCDF4 as nc
import time as t
import os
import tkinter as tk
import shutil


def chirps_download(start_date, end_date, out_folder, gui):

    gui.out_textbox.configure(state='normal')
    gui.out_textbox.delete('1.0', tk.END)
    gui.out_textbox.insert(tk.END, "Comenzando descarga...\n")
    t_start = t.perf_counter()
    shutil.rmtree(out_folder)
    os.mkdir(out_folder)

    start_date = datetime.datetime.combine(start_date, datetime.time.min)
    end_date = datetime.datetime.combine(end_date, datetime.time.min)

    server_url = 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p25/'

    start_year = start_date.year
    end_year = end_date.year

    year_int = end_year - start_year
    year_p = 0

    for year in range(start_year, end_year + 1, 1):
        filename = f"chirps-v2.0.{year}.days_p25.nc"
        file_url = server_url + filename
        with requests.Session() as session:
            req = session.request('get', file_url)
            r = session.get(req.url)
            with open(out_folder + filename, 'wb') as file:
                file.write(r.content)
        print(f"Archivo {filename} Descargado")

        # Periodos del año

        start_interval = 0
        end_interval = 0

        if start_date.year == year and end_date.year == year:

            start_interval = (start_date - datetime.datetime(start_date.year, 1, 1)).days
            end_interval = (end_date - datetime.datetime(start_date.year, 1, 1)).days

        elif start_date.year < year and end_date.year > year:
            start_interval = 0
            end_interval = (datetime.datetime(year, 12, 31) - datetime.datetime(year, 1, 1)).days

        elif start_date.year == year and end_date.year > year:
            start_interval = (start_date - datetime.datetime(start_date.year, 1, 1)).days
            end_interval = (datetime.datetime(year, 12, 31) - datetime.datetime(start_date.year, 1, 1)).days

        elif start_date.year < year and end_date.year == year:
            start_interval = 0
            end_interval = (end_date - datetime.datetime(year, 1, 1)).days

        with nc.Dataset(out_folder + filename) as ds:

            time = ds['time'][:]

            sc = ds['time'].units.find('since')
            canon_date_str = ds['time'].units[sc + 6:]
            canon_date = datetime.datetime.strptime(canon_date_str, '%Y-%m-%d  %H:%M:%S')
            for i in range(start_interval, end_interval + 1):

                current_date = str(canon_date + datetime.timedelta(days=int(time[i])))
                current_date = current_date[:10]

                file_name = "chirps-v2.0." + current_date + "_p25.nc"
                new_nc_file_dir = out_folder + file_name

                with nc.Dataset(new_nc_file_dir, 'w', format='NETCDF4') as new_ds:

                    new_ds.setncatts(ds.__dict__)

                    new_ds.createDimension('time', 1)
                    new_ds.createDimension('latitude', len(ds['latitude'][:]))
                    new_ds.createDimension('longitude', len(ds['longitude'][:]))

                    toexclude = ['precip', 'time']

                    for name, variable in ds.variables.items():
                        if name not in toexclude:
                            x = new_ds.createVariable(name, variable.datatype, variable.dimensions)
                            new_ds[name][:] = ds[name][:]
                            new_ds[name].setncatts(ds[name].__dict__)
                        elif name == 'time':
                            x = new_ds.createVariable(name, variable.datatype, variable.dimensions)
                            new_ds[name][:] = ds[name][i]
                            new_ds[name].setncatts(ds[name].__dict__)
                        elif name == 'precip':
                            x = new_ds.createVariable(name, variable.datatype, variable.dimensions)
                            new_ds[name][:] = ds[name][i]
        os.remove(out_folder + filename)

        t_end = t.perf_counter()
        toe = t_end - t_start
        gui.out_textbox.insert(tk.END, 'Descarga finalizada. \n')
        gui.out_textbox.insert(tk.END, 'Tiempo de ejecución:{toe:.2f} s\n'.format(toe=toe))
        gui.out_textbox.insert(tk.END, "Archivos guardados en: \n" + out_folder)
        gui.out_textbox.configure(state='disabled')
        gui.root.update()


if __name__ == '__main__':
    sd = datetime.datetime(1998, 12, 29)
    ed = datetime.datetime(2000, 1, 15)
    out_f = "D:\Downloads\chirps_test/"
    chirps_download(sd, ed, out_f)
