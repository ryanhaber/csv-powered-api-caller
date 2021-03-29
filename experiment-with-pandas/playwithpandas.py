import pandas as pd
import json
import sys

# get input and output files from commandline
inputfile = sys.argv[1]
outputfile = sys.argv[2]

# load the CSV, convert it to json, then build a python dictionary from the json
dataframe = pd.read_csv(inputfile)
dataInJson = dataframe.to_json(orient='records')  #build the json record-wise rather than column-wise
dataAsDict = json.loads(dataInJson)


# go through each record and replace one value with the object {'value': XYZ} just like Formability's API expects
for record in dataAsDict:
	value = record['TEMAIL']
	record['TEMAIL'] = {'value' : value}

# convert back to json string for saving to a file
dataInJson = json.dumps(dataAsDict)

# save to file
outfile = open(outputfile, 'w')
outfile.write(dataInJson)
outfile.close()