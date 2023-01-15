import boto3
import os
import datetime
import time
from botocore import UNSIGNED
from botocore.config import Config


def f():
    st = time.perf_counter()
    bucket_name = 's3-radaresideam'
    subfolder = 'l2_data/'
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    object_key = 'Bogota'

    start_date = datetime.date(2018, 6, 12)
    today = datetime.date.today()
    date_list = []
    delta = today - start_date
    sel_date = []
    dates_without_data = []
    for i in range(delta.days + 1):
        date = start_date + datetime.timedelta(days=i)
        date_list.append(date)
        prefix = subfolder+"{:04d}".format(date.year)+'/'+"{:02d}".format(date.month)+'/'+"{:02d}".format(date.day)+'/'
        response = s3.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
        try:
            radars = response['CommonPrefixes']
            for radar in radars:
                radar_name = radar['Prefix'].split('/')[-2]
                if radar_name == object_key:
                    sel_date.append(date)
        except:
            dates_without_data.append(date)
    with open('dates.txt', 'w') as file:
        for i in dates_without_data:
            file.write(str(i)+'\n')



    # def search_folder(prefix):
    #     response = s3.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
    #
    #     keys = []
    #     for year in response['CommonPrefixes']:
    #         months = s3.list_objects(Bucket=bucket_name, Prefix=year['Prefix'], Delimiter='/')
    #         for month in months['CommonPrefixes']:
    #             days = s3.list_objects(Bucket=bucket_name, Prefix=month['Prefix'], Delimiter='/')
    #             for day in days['CommonPrefixes']:
    #                 radar_list = s3.list_objects(Bucket=bucket_name, Prefix=day['Prefix'], Delimiter='/')['CommonPrefixes']
    #                 for radar in radar_list:
    #                     radar_name = radar['Prefix'].split('/')[-2]
    #                     if radar_name == object_key:
    #                         print(radar_name)
    #
    #
    #
    # search_folder(subfolder)
    et = time.perf_counter()
    dt = et-st
    print(dt)



if __name__ == '__main__':
    f()



