import boto3


def generate_bucket(bucket_name):

    s3 = boto3.resource('s3')

    s3.create_bucket(
        ACL='public-read-write',
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2'
        }
    )

    # print out all buckets created so far
    for i in s3.buckets.all():
        print(i.name)
