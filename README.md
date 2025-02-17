# aws-instance-metadata-retrieval
AWS Instance Metadata Retrieval Script
This python script retrieved AWS EC2 instance metadata using the Instance Metadata Service (IMDS).
It supports retrieving single or multiple metadata keys, listing available keys and fetching all metadata in JSON format.

## Prerequisites
- Python 3.x
- requests library (install using 'pip3 install requests')

## Usage
To retrieve metadata from AWS instance, run the python script from inside the EC2 instance.
Running this script outside the EC2 instance will not work as IMDS is only available within EC2 instance.
```sh
python3 metadata-retrieval.py
```
You have 3 options
1. If you have specific metadata key(s) you want to retrieve, just enter metadata keys (comma or space-separated) e.g. `instance-type, hostname` or `instance-type hostname`
2. If you want to retrieve all metadata, enter `'all'`
3. If you want to see first for the list of available metadata keys, enter `'list'`

## Example Output
```sh
{
    "ami-id": "ami-039454xxxxxxxxx",
    "ami-launch-index": "0",
    "hostname": "ip-xxx-xx-xx-xxx.ap-southeast-1.compute.internal",
}
```
There are also other ways to retrieve instance metadata information such as using boto3 or aws-cli (ec2 describe-instances, rds describe-db-instances for example) but this will require AWS credentails with appropriate IAM roles.
