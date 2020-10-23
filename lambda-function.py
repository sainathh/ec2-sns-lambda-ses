import json
import boto3

def lambda_handler(event, context):
    print(event['Records'][0])
    sns=event['Records'][0]['Sns']['Message']
    subject=event['Records'][0]['Sns']['Subject']
    print(sns)
    print(subject)
    client=boto3.client('ses')
    response = client.send_email(
    Destination={
        'ToAddresses': ['reciever@gmail.com', 'reciever@example.com'],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': sns,
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': subject,
        },
    },
    Source='example@gmail.com',
)

