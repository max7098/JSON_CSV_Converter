import sys

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
            #comma delimters

        lineValues = line.replace('\n','').split(',')
        lineData = {}
        for i in range(len(lineValues)):
            lineData[columns[i]]=lineValues[i]
        outfile.write(str(lineData))
    outfile.write(']')
