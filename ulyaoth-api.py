import json
import datetime
import pytz

def lambda_handler(event, context):
    # The input that comes from API Gateway.
    choice = event['params']['path']['choice']
    region = event['params']['path']['region']
    zone = event['params']['path']['zone']
    
    # This if statement handles the time requests from /time/.
    if choice == "time":
        t = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).time().replace(microsecond=0))
        return {
            'time' : t
        }
        exit()
    
    # This if statement handles the date requests from /date/.
    if choice == "date":
        d = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).date())
        return {
            'date' : d
        }
        exit()
        
    # This if statement handles the date & time requests from /datetime/.
    if choice == "datetime":
        t = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).time().replace(microsecond=0))
        d = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).date())
        return {
            'date' : d,
            'time' : t
        }
        exit()
    
    # This if statement handles date & time in iso format from /iso/.
    if choice == "iso":
        iso = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat())
        return {
            'iso' : iso
        }
        exit()