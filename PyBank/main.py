# Modules
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv"

# Open the CSV
with open(csvpath, newLine="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Loop through looking for the calculations to print
    for row in csvreader:
        #if row[0] == variable
        
        # Total number of months included int he dataset (part of column 1)
        
        # Net total amount of "Profit/Losses" (column 2) over the entire period
        
        # Average of the changes in "Profit/Losses" (column 2) over the entire period
        
        # Greatest increase in profits (date and amount) over the entire period
        
        # Greatest decrease in losses (date and amount) over the entire period
        
# Print final report as shown in example in homework instructions

# Export text file with the results