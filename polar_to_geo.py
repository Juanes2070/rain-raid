import wradlib as wrl
import numpy as np
import netCDF4 as nc
import os
import xarray as xr


def antenna_to_grid(file_route: str, interpolate: str, var: str, azimuth_var, range_var, ant_lat_var, ant_lon_var):
    with nc.Dataset(file_route, mode='a') as ds:
        data = ds[var][:360]
        ran = ds[range_var][:]
        az = np.linspace(0, 360, 361)[0:-1]
        lat = ds[ant_lat_var][:]
        lon = ds[ant_lon_var][:]

        if interpolate == 'IDW':
            data = wrl.ipol.interpolate_polar(data, ipclass=wrl.ipol.Idw)

        if interpolate == 'Linear':
            data = wrl.ipol.interpolate_polar(data, ipclass=wrl.ipol.Linear)

        if interpolate == 'Kriging':
            data = wrl.ipol.interpolate_polar(data, ipclass=wrl.ipol.OrdinaryKriging)

        if interpolate == 'Nearest':
            data = wrl.ipol.interpolate_polar(data, ipclass=wrl.ipol.Nearest)

        proj_wgs84 = wrl.georef.epsg_to_osr(4326)
        radar_location = (lon, lat, 0)
        polargrid = np.meshgrid(ran, az)

        coords = wrl.georef.spherical_to_proj(polargrid[0], polargrid[1], 0, radar_location, proj_wgs84)

        x = coords[..., 0]
        y = coords[..., 1]

        xgrid = np.linspace(x.min(), x.max(), 2000)
        ygrid = np.linspace(y.min(), y.max(), 2000)
        grid_xy = np.meshgrid(xgrid, ygrid)
        grid_xy = np.vstack((grid_xy[0].ravel(), grid_xy[1].ravel())).transpose()

        xy = np.concatenate([x.ravel()[:, None], y.ravel()[:, None]], axis=1)
        gridded = wrl.comp.togrid(
            xy,
            grid_xy,
            max(ds['range'][:].data),
            np.array([x.mean(), y.mean()]),
            data.ravel(),
            wrl.ipol.Nearest,
        )
        gridded = np.ma.masked_invalid(gridded).reshape((len(xgrid), len(ygrid)))
        gridded[np.where(gridded == -9999.0)] = np.nan

        ds.createDimension('gridded_latitude', len(xgrid))
        ds.createDimension('gridded_longitude', len(ygrid))

        out_lat = ds.createVariable('gridded_latitude', "f4", ('gridded_latitude',))
        out_lon = ds.createVariable('gridded_longitude', "f4", ('gridded_longitude',))
        out_ref = ds.createVariable('gridded_reflectivity', "f4", ('gridded_latitude', 'gridded_longitude'))

        out_lat[:] = ygrid
        out_lon[:] = xgrid
        out_ref[:, :] = gridded


def grid_to_tif(file_route, out_folder):
    file_name = os.path.basename(file_route).split('.')[0]
    ncfile = xr.open_dataset(file_route)
    pr = ncfile['gridded_reflectivity']
    pr = pr.rio.set_spatial_dims('gridded_longitude', 'gridded_latitude')
    pr.rio.set_crs("epsg:4326")

    pr.rio.to_raster(out_folder + file_name + ".tif")


if __name__ == '__main__':
    file_route = r"D:\Downloads\AWS_TEST\netCDF\BAR200916212504.nc"
    antenna_to_grid(file_route, interpolate=False)
