from google.cloud import storage
import os
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = os.environ.get('BUCKET_NAME')

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    blob_list = []

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        blob_list.append(blob.name)

    print(blob_list)

    return blob_list

def start():

    list_blobs(BUCKET_NAME)


if __name__=='__main__':

    start()