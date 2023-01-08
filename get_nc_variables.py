import netCDF4 as nc

def get_nc_variables(in_file):
    try:
        with nc.Dataset(in_file) as ds:
            vars = ds.variables.keys()
            return list(vars)
    except:
        return False

if __name__ == '__main__':
    get_nc_variables(r"D:\Downloads\AWS_TEST\netCDF\CEM200916130002.nc")