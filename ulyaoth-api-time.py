import json
import datetime
import pytz

def lambda_handler(event, context):
    # The input that comes from API Gateway.
    region = event['params']['path']['region']
    zone = event['params']['path']['zone']
    
    # The choice input is optional so we must verift it exists
    if 'choice' in event['params']['path']:
        choice = event['params']['path']['choice']
    else:
        choice = False

    if choice == "iso":
        # If a person does add /iso/ we will show the time in iso format.
        iso = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat())
        return {
            'iso' : iso
        }
        exit()
    else:
        # standard time from for example /time/europe/stockholm
        t = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).time().replace(microsecond=0))
        return {
            'time' : t
        }
        exit()