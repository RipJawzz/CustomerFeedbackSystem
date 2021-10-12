import boto3
client = boto3.client('rds')

response = client.create_db_instance(
    DBName='feedback',
    DBInstanceIdentifier='feedback',
    AllocatedStorage=10,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='feedback',
    AvailabilityZone='us-east-1a',
    BackupRetentionPeriod=0,
    EngineVersion='8.0.23',
    VpcSecurityGroupIds=[
        'sg-0bd3e0fe3c6441066',
    ],
    PubliclyAccessible=True,
    StorageType='standard',
    StorageEncrypted=False,
)

print(response['DBInstance'])