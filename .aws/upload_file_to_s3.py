import boto3


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False


uploaded = upload_to_aws(
    '../example.parquet', 'convex-bucket1', 'example.parquet'
)
