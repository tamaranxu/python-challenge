# Modules to import data
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv"

# lists to store data
voter_id = []
candidates = []
unique_candidates = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # read the header row first
    csv_header = next(csvreader)
    
    # loop through rows in data
    for row in csvreader:
        
        # add voter id column to list
        voter_id.append(row[0])
        
        # add candidate column to list
        candidates.append(row[2])
        
        # check to see if candidate name already exists in unique list
        if row[2] not in unique_candidates:
            
            # add value to unique list
            unique_candidates.append(row[2])
    
print(unique_candidates)