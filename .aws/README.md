#### Note: I am usuming you are gong to be running the scripts using Mac of Linux operating systems.

# Instructions for installation


## 1. Create a virtual environment

`virtualenv --python=<path-to-python3> venv`

## 2. activate virtual environment

`source venv/bin/activate`

## 3. Clone the code from GitHub

`git clone git@github.com:Seraph2000/convex_tech_test.git`

## 4. Install dependencies

# Instructions for operating the scripts

## 1. Run the scripts in the following order, like so

### i. Create a Parquet file locally, with some data in it. Run the following command ti do this:

#### `python create_parquet_file.py`


## 2. Create an S3 bucket, and uploads the parquet file to the bucket.

### i. Make sure you're properly connected to AWS via the terminal, by running Amazon's configuration tool, like so, and following the wizard. You'll be asked for credentials corresponding to the user you want to connect to.

### `configure aws cli`

### ii. To generate the bucket enter:

### `python generate_bucket.py`

## 3. Create an IAM Role that gives Read & List access to the S3 bucket and upload the parquet file to the bucket. Run the following command:

### i. `python `


## 4. Spin up an EC2 instance that has the above IAM Role attached


## 5. Install R on the EC2 instance and generate a parquet reader script


## 7. Run the “Parquet Reader” R Script, inside the EC2 instance

