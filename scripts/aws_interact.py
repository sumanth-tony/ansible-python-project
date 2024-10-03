import boto3

# Create EC2 instance
def create_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-0abcdef12345abcde',  # Replace with correct AMI
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    print(f'Created instance {instance[0].id}')
