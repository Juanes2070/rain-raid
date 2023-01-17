import netCDF4 as nc
import res_path


def find_index(vector, target_value, threshold):
    for i, value in enumerate(vector):
        upper_lim = round(target_value + threshold, 2)
        lower_lim = round(target_value - threshold, 2)
        if upper_lim >= round(float(value), 2) >= lower_lim:
            return i


def coord_index(target_coords):
    def_route = res_path.resource_path('res/3B-HHR.MS.MRG.3IMERG.20150501-S000000-E002959.0000.V06B.HDF5.nc4')
    with nc.Dataset(def_route, 'r') as ds:
        lat = ds['lat'][:]
        lon = ds['lon'][:]
        threshold = 0.5
        index_list = []
        for j in range(len(target_coords)):
            if (j + 1) % 2 == 0:
                index_list.append(find_index(lat, target_coords[j], threshold))
            else:
                index_list.append(find_index(lon, target_coords[j], threshold))
    return index_list
