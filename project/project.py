import boto3
session=boto3.Session(profile_name='pythonautomation')
s3=session.resource('s3')

if __name__ == '__main__':
    for i in s3.buckets.all():
        print(s3)
