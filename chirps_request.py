import requests
import datetime
import netCDF4 as nc
import time as t
import os
import cut_chirps
import out_textbox_write


def chirps_download(start_date, end_date, out_folder, bound_box, gui):

    out_textbox_write.write(gui.out_textbox, "Comenzando descarga...\n", True)
    t_start = t.perf_counter()

    start_date = datetime.datetime.combine(start_date, datetime.time.min)
    end_date = datetime.datetime.combine(end_date, datetime.time.min)

    server_url = 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p25/'

    start_year = start_date.year
    end_year = end_date.year


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
                cut_chirps.coord_index(bound_box, new_nc_file_dir, out_folder)
                #os.remove(new_nc_file_dir)
        os.remove(out_folder + filename)


        t_end = t.perf_counter()
        toe = t_end - t_start
        str_out = 'Descarga finalizada. \n'+'Tiempo de ejecución:{toe:.2f} s\n'.format(toe=toe)+"Archivos guardados en: \n" + out_folder
        out_textbox_write.write(gui.out_textbox, str_out)
        gui.root.update()


if __name__ == '__main__':
    sd = datetime.datetime(1998, 12, 29)
    ed = datetime.datetime(2000, 1, 15)
    out_f = "D:\Downloads\chirps_test/"
    chirps_download(sd, ed, out_f)
