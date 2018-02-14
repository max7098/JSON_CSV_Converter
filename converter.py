import sys
import ast

#Get file names
if len(sys.argv)<3:
    raise Exception('Missing name of infile or outfile')
infileName = sys.argv[1]
outfileName = sys.argv[2]

#Check if it is a csv to json or vice versa
if infileName.endswith('.csv') and outfileName.endswith('.json'):
    #Convert CSV to JSON
    infile = open(infileName,"r")
    outfile = open(outfileName, "w")
    #Find Column names
    columns = infile.readline().replace('\n','').split(',')

    #put data in json format
    first = True
    for line in infile:
        if first:
            first = False
            outfile.write('[')
        else:
            outfile.write(',')

        lineValues = line.replace('\n','').split(',')
        lineData = {}
        for i in range(len(lineValues)):
            lineData[columns[i]]=lineValues[i]
        outfile.write(str(lineData))
    outfile.write(']')
elif infileName.endswith('.json') and outfileName.endswith('.csv'): 
    #Convert JSON to CSV
    infile  =  open(infileName, "r")
    jsonPairs = ast.literal_eval(infile.read())

    #agregate the data to calculate columns 
    columns = set()
    for lineJSON in jsonPairs:
        columns.update(lineJSON.keys())
    columns = list(columns)

    #input data in the csv
    outfile = open(outfileName, "w")
    outfile.write(','.join(columns))
    for lineJSON in jsonPairs:
        #finds each columns corrosponding value
        lineData = map(lambda column:lineJSON[column],columns)
        outfile.write('\n')
        outfile.write(','.join(lineData))
else:
    raise Exception('Needs both a JSON and CSV file')

print("File Created: " + outfileName)
