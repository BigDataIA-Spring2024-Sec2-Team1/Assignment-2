import boto3
import os

def upload_file_to_s3(file_path, bucket_name, object_name, size):
    s3 = boto3.client('s3')
    try:
        metadata = {
            "file_name": object_name.split("/")[1],
            "type": "txt",
            "size": f"{size} Byte"
            }
        s3.upload_file(file_path, bucket_name, object_name, ExtraArgs={"Metadata": metadata})
        print(f"File uploaded successfully to S3 bucket '{bucket_name}' with key '{object_name}'")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

bucket_name = 'bigdata-assignment2'
folder_path = ['PyPDF', 'Grobid', 'CSV']

for folder in folder_path:
    files = (file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file)))
    for file in files:
        print("Uploading file", file)
        file_stats = os.stat(f"{folder}/{file}")
        upload_file_to_s3(f"{folder}/{file}", bucket_name, f"{folder}/{file}", file_stats.st_size)
