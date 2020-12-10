import pandas as pd
import json
import sys
from lib import csv_to_record

inputfile = sys.argv[1]
outputfile = sys.argv[2]


convertToDict = csv_to_record.csv_to_record(inputfile)

print("There are ", len(convertToDict), " records.")

convertToJson = json.dumps(convertToDict)

# save to file
outfile = open(outputfile, 'w')
outfile.write(convertToJson)
outfile.close()