import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instance = ec2.create_instances(
        ImageId=AMI,  # Corrigido de ImageID para ImageId
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,  # Corrigido de SubnetID para SubnetId
        MaxCount=1,
        MinCount=1
    )
    
    print('Nova instância criada:', instance[0].id)  # Corrigido para usar 'instance' corretamente

    # Retornar uma resposta adequada, se necessário
    return {
        'statusCode': 200,
        'body': 'Nova instância criada com sucesso!'
    }
