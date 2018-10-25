                  import boto3
                                     session=boto3.Session(profile_name=pythonautomation)
                                     ec2=session.resource('ec2')
                                     key_name='python_automation_key'
                                                                                              key_path=key_name+".pem"
 key=ec2.create_key_pair(KeyName=key_name)
key.key_material
                       with open(key_path,'w') as k:
                               k.write(key.key_material)
import os,stat
os.chmod(key_path,stat.S_IRUSR | stat.S_I  /*  giving permissions to only user to read,write the file with python os,stat modulle*/

list(ec2.images.filter(Owners=['amazon']))
img=ec2.Image('ami-0922553b7b0369273')
instance = ec2.create_instances( ImageId='ami-15e9c770', MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName="xyz", Placement={'AvailabilityZone':'us-east-2b'})
