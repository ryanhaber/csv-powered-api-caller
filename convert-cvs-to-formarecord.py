import pandas as pd
import json
import sys
from lib import csv_to_record




# --------------------- Get input and output names --------------------
# ATM there is no to-file output

inputfile = input("Enter the name of the .CSV file: ")

if inputfile[-4:].upper() != ".CSV":
	print("You must pick a .csv file")
	exit()

outputfile = inputfile[:-4] + ".json"

print("Keep default output filename: ", outputfile, "? (press Enter to keep or type another name and then press enter)" )
newname = input()

if newname != "":
	outputfile = newname

print("Output filename: ", outputfile)




# --------------------- Process csv file --------------------

listOfCodes = csv_to_record.csv_to_record(inputfile)
listOfOutputs = []
outputsCount = 0




# --------------------- Bundle records into groups of 100 and make API request --------------------

for item in listOfCodes:

	if outputsCount < 100:
		listOfOutputs.append(item)
		outputsCount = outputsCount + 1

	if outputsCount == 100:
		csv_to_record.api_to_formability(listOfOutputs)
		# print(listOfOutputs)
		pause = input()
		outputsCount = 0
		listOfOutputs = []

# Final request for remaining records 
csv_to_record.api_to_formability(listOfOutputs)
# print(listOfOutputs)


		


# --------------------- Test by outputting to file rather than make API call ---------------------

# convertToJson = json.dumps(convertToDict)

# # save to file
# outfile = open(outputfile, 'w')
# outfile.write(convertToJson)
# outfile.close()