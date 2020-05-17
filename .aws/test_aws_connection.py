from __future__ import print_function
import boto3
# import os

# os.environ['AWS_PROFILE'] = "default"
# os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

s3 = boto3.client('s3')

# Retrieves all regions/endpoints that work with EC2
response = s3.describe_regions()
print('Regions:', response['Regions'])



# configure aws cli - using Amazon's quick configuration



