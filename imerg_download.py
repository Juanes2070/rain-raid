# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:29:03 2022

@author: Juanes
"""

import requests
import datetime
from bs4 import BeautifulSoup
import tkinter as tk


def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


def get_imerg_links(start_date, end_date):
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


def get_imerg_file(file_url, user, psswrd, out_folder):
    with requests.Session() as session:
        req = session.request('get', file_url)
        r = session.get(req.url, auth=(user, psswrd))
        name_start = file_url.find('3B-HHR')
        first_name = file_url[name_start:]
        with open(out_folder + first_name, 'wb') as file:
            file.write(r.content)
        return first_name


def main_imerg(start_date, end_date, out_folder, user, psswrd, gui):
    links = get_imerg_links(start_date, end_date)
    total_count = len(links)
    gui.out_text.insert(tk.END, total_count)
    gui.out_text.insert(tk.END, " Archivos encontrados, comenzando descarga\n")
    gui.root.update()
    f_processed = 0
    for link in links:
        file_name = get_imerg_file(link, user, psswrd, out_folder)
        gui.out_text.insert(tk.END, file_name +" Descargado")
        gui.out_text.insert(tk.END, "\n")
        f_processed += 1
        percent = (f_processed / total_count) * 100
        gui.progressbar['value'] = percent
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
