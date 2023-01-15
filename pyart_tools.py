from pyart import io
import netCDF4 as nc
import os
import polar_to_geo


def raw_to_netcdf(in_file,out_folder,interpolate):

    file_name = os.path.basename(in_file).split('.')[0]
    out_route = out_folder+file_name+".nc"
    radar = io.read(in_file)
    io.write_cfradial(filename=out_route,
                            radar=radar,
                            format='NETCDF4',
                            time_reference=False)



if __name__ == '__main__':
    file_path = r"D:\Downloads\pyart_test\CEM200916235306.RAW2SGY"
    out_folder = r"D:\Downloads\pyart_test2/"

    raw_to_netcdf(file_path,out_folder)

