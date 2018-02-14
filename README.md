This is a Bidirectional JSON CSV data file converter.

Usage

run : 
python converter.py infile outfile

The program will use the file types to know what the data conversion it should use. 

Format 

If converting from JSON to CSV, it will use all the keys as columns in the csv file.
As such if there are many different keys among different JSON elements there will be many 
different columns and the conversion will be more computationaly expensive.

If converting from csv to JSON, it will use the columns as key values. 
Note order of columns is not gaurenteed to be maintained in JSON.

Run Time:

The run time from CSV to JSON is O(n*m) where n is the number of columns 
and m is the number of rows in the CSV.

The run time from JSON to CSV is O(n*m) where n is the number of unique keys
and m is the number of json elements. Though in practice JSON to CSV is 
about twice as computationaly expensive as CSV to JSON.
