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
    
# calculate total number of votes cast; length of list
total_votes = len(voter_id)

# create a complete list of candidates who received votes
print(unique_candidates)

# list comprehension with conditional to find all occurences of each candidate in
# candidates list and use len function to total the number
Khan_votes = len([candidate for candidate in candidates if candidate == "Khan"])
print(Khan_votes)

Correy_votes = len([candidate for candidate in candidates if candidate == "Correy"])
print(Correy_votes)

Li_votes = len([candidate for candidate in candidates if candidate == "Li"])
print(Li_votes)

OTooley_votes = len([candidate for candidate in candidates if candidate == "O'Tooley"])
print(OTooley_votes)

# calculate % of total votes for each candidate, rounded to 3 decimals
Khan_percent = round(((Khan_votes/total_votes) * 100), 3)
print(Khan_percent)

Correy_percent = round(((Correy_votes/total_votes) * 100), 3)
print(Correy_percent)

Li_percent = round(((Li_votes/total_votes) * 100), 3)
print(Li_percent)

OTooley_percent = round(((OTooley_votes/total_votes) * 100), 3)
print(OTooley_percent)