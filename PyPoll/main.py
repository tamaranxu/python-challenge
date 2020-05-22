# Modules to import data
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv"

# lists to store original data
voter_id = []
candidates = []

# new list to store unique candidates
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

# ran print function on unique_candidates list to identify names for next steps
# deleted in final code since did not need to print to terminal

# list comprehension with conditional to find all occurences of each candidate in
# candidates list and use len function to total the number
Khan_votes = len([candidate for candidate in candidates if candidate == "Khan"])
Correy_votes = len([candidate for candidate in candidates if candidate == "Correy"])
Li_votes = len([candidate for candidate in candidates if candidate == "Li"])
OTooley_votes = len([candidate for candidate in candidates if candidate == "O'Tooley"])

# calculate % of total votes for each candidate, rounded to 3 decimals
Khan_percent = round(((Khan_votes/total_votes) * 100), 3)
Correy_percent = round(((Correy_votes/total_votes) * 100), 3)
Li_percent = round(((Li_votes/total_votes) * 100), 3)
OTooley_percent = round(((OTooley_votes/total_votes) * 100), 3)

# create list for vote percents for each candidate
vote_percents = [Khan_percent, Correy_percent, Li_percent, OTooley_percent]

# zip together unique candidates lists and vote percents list to be able to find winner
final_percents = zip(unique_candidates, vote_percents)

# set initial winning value at 0, to prepare to loop through zipped list values
winning_value = 0

# loop through zipped lists (final_percents)
for row in final_percents:
    
    # find highest winning value and corresponding candidate
    if row[1] > winning_value:
        winning_value = row[1]
        winner = row[0]
        
# print results to terminal
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-----------------------------")
print(f"Khan: {str(Khan_percent)}% ({str(Khan_votes)})")
print(f"Correy: {str(Correy_percent)}% ({str(Correy_votes)})")
print(f"Li: {str(Li_percent)}% ({str(Li_votes)})")
print(f"O'Tooley': {str(OTooley_percent)}% ({str(OTooley_votes)})")
print("-----------------------------")
print(f"Winner: {str(winner)}")
print("-----------------------------")

# export text file with same results
# set variable for output file
output_file = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyPoll\Analysis\poll_results.csv"

# Open the output file
# newline="" is used to take out space in between rows
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the results; add brackets to keep comma from separating characters in string
    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Total Votes: {str(total_votes)}"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Khan: {str(Khan_percent)}% ({str(Khan_votes)})"])
    writer.writerow([f"Correy: {str(Correy_percent)}% ({str(Correy_votes)})"])
    writer.writerow([f"Li: {str(Li_percent)}% ({str(Li_votes)})"])
    writer.writerow([f"O'Tooley': {str(OTooley_percent)}% ({str(OTooley_votes)})"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Winner: {str(winner)}"])
    writer.writerow(["-----------------------------"])