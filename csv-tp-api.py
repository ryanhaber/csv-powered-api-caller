import csv
import json
import requests

# read CSV
# River will write code to do this

# assemble JSON
# this is the flow chart

headerObject = {}

for row in csvFile:
	record = headerObject
	for field in record:
		# XYZ
	# add record to jsonArray


# make API request
# Ryan will write code to do this

url = 'https://maryland.formability.enovationallabs.com/api/v2/object_models/5f10a8b40c6fd700fe4baebb/records?='
urlParams = {'key1': 'value1', 'key2': 'value2'}
body = {'key':'value'}

requestResult = requests.post(url, params = urlParams, data = body)

# validate response

# issue any alerts necessary