import wradlib as wrl
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# We will export this RADOLAN dataset to a GIS compatible format
wdir = wrl.util.get_wradlib_data_path() + "/radolan/grid/"
filename = "radolan/misc/raa01-sf_10000-1408102050-dwd---bin.gz"
filename = wrl.util.get_wradlib_data_file(filename)
data_raw, meta = wrl.io.read_radolan_composite(filename)

proj_osr = wrl.georef.create_osr("dwd-radolan")

# Get projected RADOLAN coordinates for corner definition
xy_raw = wrl.georef.get_radolan_grid(900, 900)
data, xy = wrl.georef.set_raster_origin(data_raw, xy_raw, "upper")


if __name__ == '__main__':
    pass