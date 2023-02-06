import os
import time
import requests
import datetime
import shutil
import out_textbox_write
import netcdf_cut
import multiprocessing as mp
from bs4 import BeautifulSoup
from itertools import repeat


def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


def get_imerg_links(start_date, end_date):
    start_date = datetime.datetime.combine(start_date, datetime.time.min)
    end_date = datetime.datetime.combine(end_date, datetime.time.min)

    server_url = 'https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3IMERGHH.06/'
    interval_number = (end_date - start_date).days + 1
    file_urls = []
    for i in range(interval_number):
        date_list = []
        date_list.append(start_date + datetime.timedelta(days=i))
        for date in date_list:
            year = date.year
            zero_date = datetime.datetime(year, 1, 1)
            delta_day = (date - zero_date).days + 1
            day_number = "{:03d}".format(delta_day)
            days_url = server_url + str(year) + "/" + str(day_number) + "/"
            file_names = listFD(days_url, 'HDF5')
            for file in file_names:
                name_start = file.find('3B-HHR')
                first_name = file[name_start:]
                file_url = days_url + first_name + ".nc4"
                file_urls.append(file_url)
    return file_urls


def get_imerg_file(file_url, user, psswrd, out_folder, bound_box):
    with requests.Session() as session:
        req = session.request('get', file_url)
        r = session.get(req.url, auth=(user, psswrd))
        name_start = file_url.find('3B-HHR')
        first_name = file_url[name_start:]
        file_route = out_folder + first_name
        with open(file_route, 'wb') as file:
            file.write(r.content)
        netcdf_cut.coord_index(bound_box, file_route, out_folder)
        os.remove(file_route)


def main_imerg(start_date, end_date, out_folder, user, psswrd, boundary_box, gui):
    t_start = time.perf_counter()

    shutil.rmtree(out_folder)
    os.mkdir(out_folder)

    links = get_imerg_links(start_date, end_date)
    total_count = len(links)
    start_str = str(total_count) + " Archivos encontrados, \ncomenzando descarga...\n"
    out_textbox_write.write(gui.out_textbox, start_str, True)
    gui.root.update()

    with mp.Pool() as p:
        p.starmap(get_imerg_file, zip(links,
                                      repeat(user),
                                      repeat(psswrd),
                                      repeat(out_folder),
                                      repeat(boundary_box)))

    t_end = time.perf_counter()
    toe = t_end - t_start
    end_str = 'Descarga finalizada. \n' + 'Tiempo de ejecución:{toe:.2f} s\n'.format(
        toe=toe) + "Archivos guardados en: \n" + out_folder
    out_textbox_write.write(gui.out_textbox, end_str)
    gui.root.update()


if __name__ == '__main__':
    # Year_Month_Day
    start_date = datetime.datetime(2020, 10, 1)
    end_date = datetime.datetime(2020, 10, 2)
    # Usuario y contraseña, debe tener acceso a NASA GESDISC DATA ARCHIVE
    user = 'juanes2070@gmail.com'
    password = 'Test123456'
    w_folder = 'D:\Downloads\chirps_test/'
    main_imerg(start_date, end_date, w_folder, user, password)
