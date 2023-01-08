import os
import boto3
from datetime import datetime

def get_s3_file_list(bucket_name,prefix):
    s3 = boto3.client('s3')
    object_keys = []
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    keys = []
    for key in response['Contents']:
        keys.append(key['Key'])
    while response['IsTruncated']:
        continuation_token = response['NextContinuationToken']
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix,ContinuationToken=continuation_token)
        for key in response['Contents']:
            keys.append(key['Key'])
    return keys

def get_interval_files(bucket_name,prefix,interval,threshold):

    route_list = get_s3_file_list(bucket_name,prefix)
    file_list = []
    for file in route_list:
        file_list.append(os.path.basename(file))

    file_list.sort(key=lambda x: datetime.strptime(x.split('.')[0][3:], '%y%m%d%H%M%S'))
    selected_files = []
    # Iterate over the sorted list of files
    i = 0
    k = 1
    while k < len(file_list):
        if i == 0 and k == 1:
            selected_files.append(prefix+'/'+file_list[i])

        current_timestamp = datetime.strptime(file_list[i].split('.')[0][3:], '%y%m%d%H%M%S')
        next_timestamp = datetime.strptime(file_list[k].split('.')[0][3:], '%y%m%d%H%M%S')

        delta = (next_timestamp-current_timestamp).total_seconds()/60

        if delta > interval-threshold and delta < interval+threshold:
            selected_files.append(prefix+'/'+file_list[k])
            i = k
            k +=1
        else:
            k+=1
    return selected_files

if __name__ == '__main__':
    bucket_name = 's3-radaresideam'
    prefix = 'l2_data/2020/09/16/Barrancabermeja'
    #com = 's3://s3-radaresideam/l2_data/2020/09/16/Barrancabermeja'
    print(get_interval_files(bucket_name,prefix,60,0.2))

