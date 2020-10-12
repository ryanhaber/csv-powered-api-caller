import pandas as pd
import json

d = {'name': ['ryan', 'john', 'mary'], 'age':[43,32,21]}
df = pd.read_csv('scripttestdata1.csv')

print(df)

convertToJson = df.to_json(orient='records')

convertToDict = json.loads(convertToJson)


for record in convertToDict:
	value = record['TEMAIL']
	record['TEMAIL'] = {'value' : value}

convertToJson = json.dumps(convertToDict)

outfile = open('scripttestdata1.json', 'w')
outfile.write(convertToJson)
outfile.close()