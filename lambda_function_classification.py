import json
import os
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Make a prediction:
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
    ContentType='application/x-image',
    Accept = 'application/json',
    Body=image)
                                       
    # We return the data back to the Step Function    
    # event["inferences"] = inferences
    confidence = json.loads(response['Body'].read().decode())

    return {
        'confidence': confidence
    }