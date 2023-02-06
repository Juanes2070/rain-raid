import netCDF4 as nc
import os


def find_index(vector, target_value, threshold):
    for i, value in enumerate(vector):
        upper_lim = round(target_value + threshold, 2)
        lower_lim = round(target_value - threshold, 2)
        if upper_lim >= round(float(value), 2) >= lower_lim:
            return i


def coord_index(target_coords, fd, out_folder):
    with nc.Dataset(fd) as ds:
        lat = ds['latitude'][:]
        lon = ds['longitude'][:]
        threshold = 0.5
        index_list = []
        for j in range(len(target_coords)):
            if (j + 1) % 2 != 0:
                index_list.append(find_index(lat, target_coords[j], threshold))
            else:
                index_list.append(find_index(lon, target_coords[j], threshold))
        indexes = index_list
        north = indexes[2]
        south = indexes[0]
        east = indexes[3]
        west = indexes[1]
        var = ds['precip'][0,south:north, west:east]
        new_lats = ds['latitude'][south:north]
        new_lons = ds['longitude'][west:east]

        file_name = os.path.basename(fd)
        new_nc_route = out_folder+'c_'+file_name

        with nc.Dataset(new_nc_route, 'w') as new_ds:

            new_ds.createDimension('latitude', len(new_lats))
            new_ds.createDimension('longitude', len(new_lons))

            lats = new_ds.createVariable('latitude', ds['latitude'].datatype, 'latitude')
            lons = new_ds.createVariable('longitude', ds['longitude'].datatype, 'longitude')
            prec = new_ds.createVariable('precip', ds['precip'].datatype, ('latitude', 'longitude'))

            lats[:] = new_lats
            lons[:] = new_lons
            prec[:] = var


if __name__ == '__main__':
    fd = r"D:\Downloads\Satellite_test\chirps-v2.0.2020-01-12_p25.nc"
    out_folder = r"D:\Downloads\Satellite_test/"
    test_coords = [1.5, -77.9, 3.18, -75.84]
    coord_index(test_coords, fd, out_folder)
