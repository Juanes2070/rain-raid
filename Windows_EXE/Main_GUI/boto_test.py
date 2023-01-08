import boto3
import os

s3 = boto3.client('s3')
bucket_name = 's3-radaresideam'
#bucket = client.Bucket(bucket_name)
file_name = 'l2_data/2020/09/16/Barrancabermeja/BAR200916230004.RAW2SEB'
out_file = r"D:\Downloads\BOTO_TEST\boto_test.raw2seb"

prefix = 'l2_data/2020/09/16/Barrancabermeja'
objects = s3.list_objects(Bucket=bucket_name, Prefix=prefix)
# folders = objects['CommonPrefixes']
object_keys = [obj['Key'] for obj in objects['Contents']]
print(object_keys)


s3.download_file(bucket_name, file_name, out_file)

# result = client.list_objects(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
# for o in result.get('CommonPrefixes'):
#     print('sub folder : '+ o.get('Prefix'))


# files = []
# for key in conn.list_objects(Bucket=bucket)['Contents']:
#     files.append(key['Key'])
# print('done')




if __name__ == '__main__':
    pass