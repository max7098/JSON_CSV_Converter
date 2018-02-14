This is a Bidirectional JSON CSV data file converter.

Usage
run : python converter.py infile outfile

The program will use the file types to know what the data should be converted into. 

Format :

If converting from JSON to CSV, it will use all the keys as columns in the csv file.
As such if there are many different keys among different

If converting from csv to JSON, it will use the columns as key values.
