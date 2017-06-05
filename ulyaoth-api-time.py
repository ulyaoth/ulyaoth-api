import json
import datetime
import pytz

def lambda_handler(event, context):
    # The input that comes from API Gateway.
    region = event['params']['path']['region']
    zone = event['params']['path']['zone']
    
    # The choice input is optional so we must verift it exists and we also set the endpoint url
    if 'choice' in event['params']['path']:
        choice = event['params']['path']['choice']
        endpoint = "/time/" + region + "/" + zone + "/" + choice
    else:
        choice = "false"
        endpoint = "/time/" + region + "/" + zone 
    
    # if there is no choice we show a json with everything
    if choice == "false":
        iso8601 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat())
        rfc3339 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat()) + "Z"
        data = { "meta": { "endpoint": endpoint	}, "data": { "iso8601": iso8601, "rfc3339": rfc3339 }}

        return data
        exit()
    
    # Check if the choice is iso8601
    if choice == "iso8601":
        iso8601 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat())
        data = { "meta": { "endpoint": endpoint	}, "data": { "iso8601": iso8601 }}

        return data
        exit()

    # Check if the choice is rfc3339
    if choice == "rfc3339":
        rfc3339 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat()) + "Z"
        data = { "meta": { "endpoint": endpoint	}, "data": { "rfc3339": rfc3339 }}

        return data
        exit()