from boto3 import Session

sess = Session(aws_access_key_id='AKIAXFJKPM7QDTDCL6WT',
               aws_secret_access_key='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',
              region_name="us-east-1")

# Use Amazon S3
s3 = sess.resource('s3')

# Print out all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Başka session-account için de bakılabilir.