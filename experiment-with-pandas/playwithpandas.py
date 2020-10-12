import pandas as pd
import json

# load the CSV, convert it to json, then build a python dictionary from the json
df = pd.read_csv('scripttestdata1.csv')
convertToJson = df.to_json(orient='records')  #build the json record-wise rather than column-wise
convertToDict = json.loads(convertToJson)


# go through each record and replace one value with the object {'value': XYZ} just like Formability's API expects
for record in convertToDict:
	value = record['TEMAIL']
	record['TEMAIL'] = {'value' : value}

# convert back to json string for saving to a file
convertToJson = json.dumps(convertToDict)

# save to file
outfile = open('scripttestdata1.json', 'w')
outfile.write(convertToJson)
outfile.close()