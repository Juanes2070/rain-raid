import numpy as np
import netCDF4 as nc
import os


def ref_to_int(dbz, m_disd, b_disd, b_zr, a_zr, mc3, bc3, trunc, dt):

    trunc_dbz2 = np.copy(dbz)
    c1_all = (1 / m_disd) * trunc_dbz2 - (b_disd / m_disd)
    if trunc is not None:
        c1_all[c1_all >= trunc] = trunc
    c2_all = ((10 ** (c1_all / 10.0)) / a_zr) ** (1.0 / b_zr)
    c3_all = (mc3 * c2_all + bc3)
    c3_all[c1_all <= 5.0] = 0.0

    pp = c3_all * dt / 60
    return pp


def nc_file_processing(file, ref_var, lat_var, lon_var, m_disd, b_disd, b_zr, a_zr, trunc, dt,out_folder):

    #TODO preguntar por estos valores
    # ??? Correccion precipitacion estratiforme (?
    mc3 = 1.287776431
    bc3 = 2.860530405
    with nc.Dataset(file) as ds:
        ref = ds[ref_var][:]
        lat = ds[lat_var][:]
        lon = ds[lon_var][:]
        intensity = ref_to_int(dbz=ref,
                               m_disd=m_disd,
                               b_disd=b_disd,
                               b_zr=b_zr,
                               a_zr=a_zr,
                               mc3=mc3,
                               bc3=bc3,
                               trunc=trunc,
                               dt=dt)
    name = os.path.basename(file)
    out_file = out_folder + name
    with nc.Dataset(out_file, mode='w') as out_ds:

        out_ds.createDimension('latitude', len(lat))
        out_ds.createDimension('longitude', len(lon))

        lats = out_ds.createVariable('latitude', "f4", ('latitude',))
        lons = out_ds.createVariable('longitude', "f4", ('longitude',))
        inten = out_ds.createVariable('precip', "f4", ('latitude', 'longitude'))

        lats[:] = lat
        lons[:] = lon
        inten[:] = intensity


if __name__ == '__main__':
    file = r"D:\Downloads\AWS_TEST\netCDF\BAR200916200004.nc"
    out_f = r"D:\Downloads\ref_to_pp_test/"
    nc_file_processing(file=file,
                       ref_var='gridded_reflectivity',
                       lat_var='gridded_latitude',
                       lon_var='gridded_longitude',
                       trunc=52,
                       out_folder=out_f)
