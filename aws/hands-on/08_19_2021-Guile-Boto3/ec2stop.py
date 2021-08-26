import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0e8d2b97a954250ba').stop() # put your instance id
