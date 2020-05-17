import boto3
import pprint

pp = pprint.PrettyPrinter(width=41, compact=True)


# Create an IAM Role that gives Read & List access to the S3 bucket
# https://realpython.com/python-boto3-aws-s3/

# create a client connection to iam
iam = boto3.client('iam')

# # create a user - give key, which is username
# response = iam.create_user(UserName='seraph2')

# grant iam role admin access

# # give read and list access to S3 bucket

# grant full access to S3
# Create IAM client

# response = iam.attach_role_policy(
#     PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess',
#     RoleName='ReadOnlyRole'
# )

# print("set policy: ", response)

# get arn for a given user
users = iam.get_paginator('list_users')
for response in users.paginate():
    print(response)
    for user in response['Users']:
        if user['UserName'] == 'seraph':
            user_arn = user['Arn']
            print(user['Arn'])




# # Attach a role policy
# iam.attach_role_policy(
#     PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess',
#     RoleName='seraph'
# )

# # Attach a role policy
# iam.attach_role_policy(
#     PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess',
#     RoleName='seraph'
# )


# grant full access to EC2

# # update username
# # iam.update_user(UserName="seraph", NewUserName="seraph1")


# # https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-api.html


# # STS service
# sts_client = boto3.client('sts')

# # Call the assume_role method of the STSConnection object and pass the role
# # ARN and a role session name.
# assumed_role_object = sts_client.assume_role(
#     RoleArn=user_arn,
#     RoleSessionName="AssumeRoleSession1"
# )

# # From the response that contains the assumed role, get the temporary 
# # credentials that can be used to make subsequent API calls
# credentials = assumed_role_object['Credentials']

# # Use the temporary credentials that AssumeRole returns to make a 
# # connection to Amazon S3  
# s3_resource = boto3.resource(
#     's3',
#     aws_access_key_id=credentials['AccessKeyId'],
#     aws_secret_access_key=credentials['SecretAccessKey'],
#     aws_session_token=credentials['SessionToken'],
#     region='eu-west-2'
# )

# # Use the Amazon S3 resource object that is now configured with the 
# # credentials to access your S3 buckets. 
# for bucket in s3_resource.buckets.all():
#     print(bucket.name)




#1

#2

#3
