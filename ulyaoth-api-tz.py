import json
import datetime
import pytz

def lambda_handler(event, context):
	# The input that comes from API Gateway.
	region = event['params']['path']['region']
	zone = event['params']['path']['zone']
	regionzone = region + "/" + zone

	# The first choice input is optional so we must verift it exists and we also set the endpoint url
	if 'firstchoice' in event['params']['path']:
		firstchoice = event['params']['path']['firstchoice']
	else:
		firstchoice = "false"
   
	# The second choice input is optional so we must verift it exists and we also set the endpoint url
	if 'secondchoice' in event['params']['path']:
		secondchoice = event['params']['path']['secondchoice']
	else:
		secondchoice = "false"

	if firstchoice != "false" and secondchoice == "false":
		endpoint = "/tz/" + region + "/" + zone + "/" + firstchoice
	elif firstchoice != "false" and secondchoice != "false":
		endpoint = "/tz/" + region + "/" + zone + "/" + firstchoice + "/" + secondchoice
	else:
		endpoint = "/tz/" + region + "/" + zone 

	# if there is no first choice we show a json with everything
	if firstchoice == "false":
		iso8601 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat())
		rfc3339 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat()) + "Z"
		t = datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).time().replace(microsecond=0)
		hour12 = str(t.strftime("%I:%M %p"))
		hour24 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).time().replace(microsecond=0))
		data = { "meta": { "endpoint": endpoint, "timezone": regionzone }, "data": { "12hour": hour12, "24hour": hour24, "iso8601": iso8601, "rfc3339": rfc3339 }}
		return data
		exit()  
	# Check if the first choice is to show iso8601 time format
	elif firstchoice == "iso8601":
		iso8601 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat())
		data = { "meta": { "endpoint": endpoint, "timezone": regionzone }, "data": { "iso8601": iso8601 }}
		return data
		exit()
	# Check if the first choice is to show rfc3339 time format
	elif firstchoice == "rfc3339":
		rfc3339 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).isoformat()) + "Z"
		data = { "meta": { "endpoint": endpoint, "timezone": regionzone }, "data": { "rfc3339": rfc3339 }}
		return data
		exit()
	# Check if the first choice is to show 12 hour time format
	elif firstchoice == "12hour":
		t = datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).time().replace(microsecond=0)
		hour12 = str(t.strftime("%I:%M %p"))
		data = { "meta": { "endpoint": endpoint, "timezone": regionzone }, "data": { "12hour": hour12 }}
		return data
		exit()
	# Check if the first choice is to show 24 hour time format
	elif firstchoice == "24hour":
		hour24 = str(datetime.datetime.now(pytz.timezone('%s/%s' % (region.capitalize(), zone.capitalize()))).time().replace(microsecond=0))
		data = { "meta": { "endpoint": endpoint, "timezone": regionzone }, "data": { "24hour": hour24 }}
		return data
		exit()