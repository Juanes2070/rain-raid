import boto3
import tkinter as tk
import datetime
import os
import sort_by_interval
from botocore import UNSIGNED
from botocore.config import Config
from multiprocessing import Pool
from itertools import repeat

def get_aws_folders(bucket_name,prefix):
    s3 = boto3.client('s3',config=Config(signature_version=UNSIGNED))
    objects = s3.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
    folders = objects['CommonPrefixes']
    names = []
    for folder in folders:
        folder_name = folder['Prefix'].split('/')[-2]
        names.append(folder_name)
    return names

def radar_list(start_date,end_date,gui):
    str_fromated_date = "{:04d}".format(start_date.year)+'/'+"{:02d}".format(start_date.month)+'/'+"{:02d}".format(start_date.day)+'/'
    end_fromated_date = "{:04d}".format(end_date.year)+'/'+"{:02d}".format(end_date.month)+'/'+"{:02d}".format(end_date.day)+'/'

    bucket_name = 's3-radaresideam'
    start_prefix = 'l2_data/'+str_fromated_date
    end_prefix = 'l2_data/' + end_fromated_date

    radar_start_vector = get_aws_folders(bucket_name,start_prefix)
    radar_end_vector = get_aws_folders(bucket_name, end_prefix)

    available_radar = (set(radar_end_vector).intersection(radar_start_vector))
    i = 0

    gui.avail_radar_listbox.delete(0,tk.END)

    for radar in available_radar:
        gui.avail_radar_listbox.insert(i+1,radar)
        i =+ 1
    gui.root.update()


def aws_download(file,out_folder):
    s3 = boto3.client('s3')
    bucket_name = 's3-radaresideam'
    out_file = out_folder+os.path.basename(file)
    s3.download_file(bucket_name,file,out_file)



#Toma dos fechas, nombre de radar y descarga los datos a la carpeta seleccionada
def aws_radar_download(start_date,end_date,radar_name,interval,out_folder,gui):

    n = (end_date-start_date).days+1
    # gui.out_textbox.insert(tk.END, str(n) + " días encontrados \n")
    # gui.out_textbox.insert(tk.END, "Comenzando descarga... \n")
    # gui.root.update()

    for i in range(n):
        date = start_date + datetime.timedelta(days=i)
        day_str = "{:04d}".format(date.year)+"{:02d}".format(date.month)+"{:02d}".format(date.day)
        day_folder = out_folder+day_str+"/"
        os.mkdir(day_folder)
        str_fromated_date = "{:04d}".format(date.year) + '/' + "{:02d}".format(date.month) + '/' + "{:02d}".format(date.day)
        bucket_name = 's3-radaresideam'
        prefix = 'l2_data/'+str_fromated_date+"/" + radar_name

        file_list = sort_by_interval.get_interval_files(bucket_name=bucket_name,
                                                        prefix=prefix,
                                                        interval=interval,
                                                        threshold=0.2)


        gui.out_textbox.insert(tk.END, str(len(file_list)) + " Archivos encontrados \n")
        gui.out_textbox.insert(tk.END, "Comenzando descarga de archivos RAW... \n")
        gui.root.update()


        with Pool() as p:
            p.starmap(aws_download,zip(file_list,repeat(day_folder)))


    gui.out_textbox.insert(tk.END, "Descarga finalizada \n")
    gui.root.update()



if __name__ == '__main__':
    aws_test()