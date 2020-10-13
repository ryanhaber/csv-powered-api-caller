import pandas as pd
import json
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

# load the CSV, convert it to json, then build a python dictionary from the json
df = pd.read_csv(inputfile)
convertToJson = df.to_json(orient='records')  #build the json record-wise rather than column-wise
convertToDict = json.loads(convertToJson)


# go through each record and replace one value with the object {'value': XYZ} just like Formability's API expects
for record in convertToDict:
	value = record['TEMAIL']
	record['TEMAIL'] = {'value' : value}

# convert back to json string for saving to a file
convertToJson = json.dumps(convertToDict)

# save to file
outfile = open(outputfile, 'w')
outfile.write(convertToJson)
outfile.close()