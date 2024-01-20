import os
import csv


# Set path for file
csvpath = os.path.join(bank.main.py.csv)

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    months = 0
    # Loop through to tally the months
    for row in csvreader:
        date = row[0]
        months += 1

      
print(months)  
    
