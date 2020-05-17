import boto3
import json

account_id = '842664811632'
session = boto3.session.Session(profile_name='default')
iam = session.client('iam')

path = '/'
# this needs to be unique
role_name = 'ec2-test-role-1'
# this needs to be unique
description = 'boto3 ec2 test role 1'

trust_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

response = iam.create_role(
    Path=path,
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(trust_policy),
    Description=description,
    MaxSessionDuration=3600
)

managed_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3ReadOnly",
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "Ec2FullAccess",
            "Action": "ec2:*",
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}

response = iam.create_policy(
  PolicyName='boto3-test-policy-1',
  PolicyDocument=json.dumps(managed_policy)
)

iam.attach_role_policy(
    # this needs to match policy name
    PolicyArn='arn:aws:iam::' + str(account_id) + ':policy/boto3-test-policy-1',
    # this needs to be same as rolename above
    RoleName='ec2-test-role-1'
)


# spin up an ec2 instance
