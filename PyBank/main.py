# Modules
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv"

# Create variables
# Total number of months included in the dataset; number of rows
# Net total amount of Profit/Losses
# Average Change
# Greatest Increase
# Greatest Decrease

# Open the CSV
with open(csvpath, newLine="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Loop through looking for the calculations to print
    for row in csvreader:
        #if row[0] == variable
        
        # Total number of months included in the dataset (part of column 1); number of rows?
        
        # Net total amount of "Profit/Losses" (column 2) over the entire period; add them all up?
        
        # Average of the changes in "Profit/Losses" (column 2) over the entire period
        
        # Greatest increase in profits (date and amount) over the entire period
        
        # Greatest decrease in losses (date and amount) over the entire period
        
# Print final report as shown in example in homework instructions
print(Financial Analysis)
print("-----------------------------")
# Print total months
#print("Total Months: " + variable for total number of months) 

# Export text file with the final report