# Modules to import data
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv"

# lists to store data
date = []
profit_losses = []
changes = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)

    # Set start value for previous row variable
    previous_row = 0
    
    for row in csvreader:
                
        # add date column to list
        date.append(row[0])
        
        # add profit_losses column to list as integer
        profit_losses.append(int(row[1]))
        
        # calculate difference between profit_losses column and previous row; add to list as integer
        if previous_row == 0:
            changes.append(int(0))
        else:
            changes.append(int(row[1]) - int(previous_row))
        previous_row = int(row[1])
        
# find total number of months in data set
total_months = len(date)

# find the net total of profit/losses over entire period
net_total = sum(profit_losses)

# find average of changes in profit/losses over entire period, excluding first row
average_change = sum(changes)/(len(changes)-1)

# Dictionary to store data
monthly_profit_losses = {"Month": [date], "Increase/Decrease": [changes]}