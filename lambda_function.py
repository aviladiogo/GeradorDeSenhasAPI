import json
from generator import generate

def lambda_handler(event, context):
    payload = event['queryStringParameters']["Size"]
    password = generate(int(payload))
    print(''.join(password))
    
    return {
        'statusCode': 200,
        'body': json.dumps(password)
    }
