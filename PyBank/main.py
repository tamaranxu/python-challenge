# Modules
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv"

# Create variables
# TotalMonths = ?; Total number of months included in the dataset; number of rows
# NetTotal = ?; Net total amount of Profit/Losses
# AvgChange = ?; Average Change
# IncreaseDate = ?; Greatest Increase
# IncreaseProfit = ?
# DecreaseDate = ?; Greatest Decrease
# DecreaseProfit = ?

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        print(row)
    
    # Loop through looking for the calculations to print; each row is a list
    #for row in csvreader:
        #if row[0] == variable
        
        # Total number of months included in the dataset (part of column 1); number of rows?
        # re-set TotalMonths to be next row, so that final is last row, but need to not count header row
        
        # Net total amount of "Profit/Losses" (column 2) over the entire period; add them all up?
        
        # Average of the changes in "Profit/Losses" (column 2) over the entire period
        
        # Greatest increase in profits (date and amount) over the entire period
        
        # Greatest decrease in losses (date and amount) over the entire period
        
# Print final report as shown in example in homework instructions
#print(Financial Analysis)
#print("-----------------------------")
# Print total months
#print("Total Months: " + TotalMonths)
#print("Total: $" + NetTotal)
#print("Greatest Increase in Profits: " + IncreaseDate + "( $" + IncreaseProfit + ")")
#print("Greatest Decrease in Profits: " + DecreaseDate + " ($" + DecreaseProfit + ")") 

# Export text file with the final report (see day 2 activity 5)