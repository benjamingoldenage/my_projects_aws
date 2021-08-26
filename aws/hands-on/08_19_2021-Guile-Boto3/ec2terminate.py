import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-01edc4164ba2cd204').terminate() # put your instance id
