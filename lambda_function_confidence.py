import json

THRESHOLD = 0.8

def lambda_handler(event, context):

    # Grab the inferences from the event
    inferences = event["confidence"]
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = inferences[0] > THRESHOLD or inferences[1] > THRESHOLD

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")
    
    return {
        'body': json.dumps(event)
    }