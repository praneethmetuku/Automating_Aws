import boto3
session=boto3.Session(profile_name='pythonautomation')
s3=session.resource('s3')
new_bucket=s3.create_bucket(Bucket='awspythonboto3-praneeth',CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
new_bucket
for i in s3.buckets.all():
    print(i)
