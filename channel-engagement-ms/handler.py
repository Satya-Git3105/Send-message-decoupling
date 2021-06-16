import json
import boto3
from botocore.exceptions import ClientError

region = "us-east-1"
client = boto3.client('pinpoint',region_name=region)

def execute_send_message(payload):

    print("payload : - " + payload)
    # TO DO : - Folling details like Origination nummber/desitination number 
    # Message content/senderID would get extracted  
    originationNumber = "+12342319214"
    senderId = "SENDER"
    destinationNumber = "+91991655323"
    # The content of the SMS message.
    message = ("message content")
    pinpoint_applicationId = "6a136336668a48959dd781f63344bc08"
    messageType = "PROMOTIONAL"
    # The registered keyword associated with the originating short code leave it blank if using sender IDs
    registeredKeyword = "keyword_753631027292"
    
    try:
        response = client.send_messages(
            ApplicationId=pinpoint_applicationId,
            MessageRequest={
                'Addresses': {
                    destinationNumber: {
                        'ChannelType': 'SMS'
                    }
                },
                'MessageConfiguration': {
                    'SMSMessage': {
                        'Body': message,
                        'Keyword': registeredKeyword,
                        'MessageType': messageType,
                        'OriginationNumber': originationNumber,
                        'SenderId': senderId
                    }
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Message sent! Message ID: "
                + response['MessageResponse']['Result'][destinationNumber]['MessageId'])
    return 'Success'


def lambda_handler(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    #Read from SQS queue
    for record in event['Records']:
        print("SQS iteration strarts")
        payload = record["body"]
        ## to do - customers need to curate the SQS payload thats coming from API gateway
        # and send it to  "execute_send_message" function to call Pinpoint  API. 
        execute_send_message(payload)
        print(str(payload))

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
