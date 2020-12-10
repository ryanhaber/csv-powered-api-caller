import pandas as pd
import json
import sys

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