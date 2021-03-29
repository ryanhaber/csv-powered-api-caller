import pandas as pd
import json
import sys
import requests

# inputfile is a filename as a string

def csv_to_record(inputfile):

	# load the CSV, convert it to json, then build a python dictionary from the json
	df = pd.read_csv(inputfile)
	convertToJson = df.to_json(orient='records')  #build the json record-wise rather than column-wise
	convertToDict = json.loads(convertToJson)


	# go through each record and replace each value with the object {'value': XYZ} just like Formability's API expects
	for record in convertToDict:
		for column in record:	
			value = record[column]
			record[column] = {'value' : value}

	# convert back to json string for saving to a file
	# convertToJson = json.dumps(convertToDict)

	return convertToDict


# want to add in params for path, model, token, and user
def api_to_formability(listOfRecords):

	jsonRecords = '{ "records": ' + json.dumps(listOfRecords) + "}"

	url = "https://maryland.formability-staging.enovationallabs.com/api/v2/object_models/5fd24ccdb2fc5d00fbc75cd5/records/"

	headers = {
		'Authorization': 'Bearer ',
		'Content-Type': 'application/json',
		'current-user-id': '
		}

	response = requests.request("POST", url, headers=headers, data=jsonRecords)

	print("----------------------")

	print(jsonRecords)
	print(len(listOfRecords), " records in set")

	print("Response: ")
	print(response.text)
