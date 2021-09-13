import boto3
# Use Amazon S3
s3 = boto3.resource('s3')
# Upload a new file
data = open('cat0.jpg', 'rb')
s3.Bucket('KRNDIBUCKET NAMEINIZ').put_object(Key='cat0.jpg', Body=data)  