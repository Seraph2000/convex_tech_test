from create_parquet_file import create_parquet_file
from generate_bucket import generate_bucket


# 1. Create a parquet file
create_parquet_file('example1.parquet')

# 2. Create an S3 bucket, and upload the parquet file to the bucket
generate_bucket('convex-bucket2')


#3 Create an IAM Role that gives Read & List access to the S3 bucket


#4 Spin up an EC2 instance that has the above IAM Role attached


#5 Install R on the EC2 instance


#6 Copy a “Parquet Reader” R Script to the EC2 instance

#7 Run the “Parquet Reader” R Script
#https://arrow.apache.org/docs/r/reference/read_parquet.html

# i.e. # NOT RUN {
# df <- read_parquet(system.file("v0.7.1.parquet", package="arrow"))
# head(df)
# # }

# this should be in a separate file

#######credentials########

# user can sign in at: https://842664811632.signin.aws.amazon.com/console
# access key id: AKIA4IMV4TRYE3NFTPE7
# secret access key id: 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

####watch tutorial series####
# https://www.youtube.com/watch?v=Bom9_K4m4sg







#1 create an IAM account in AWS
# login: https://842664811632.signin.aws.amazon.com/console
# access key id: AKIA4IMV4TRYKFXTYLN5
# secret access key: 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
# install boto3

#2 create a .aws folder
#3 cd into .aws & create the following two files
#4 create credentials & config
# touch credentials
# touch config
# edit the files accordingly

#3 now create the script!




# try $ aws configure
# install aws-cli
# sudo snap install aws-cli

