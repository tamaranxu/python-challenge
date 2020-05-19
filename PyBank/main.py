# store profit numbers as int(x) somehow when adding to list in for loop

# Modules
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv"

# lists to store data; how to define the data types
date = []
profit_losses = []
monthly_change = []

# define function to store calculations
#def calculations(budget_data):
    #month = str(budget_data[0])
    #budget_change = int(budget_data[1])
    

    
    # find net total of profit/losses over entire period
    #net_total = sum(profit_losses)

# AvgChange = ?; Average Change; print(average(profit_losses)); define average as function
# IncreaseDate = ?; Greatest Increase
# IncreaseProfit = ?
# DecreaseDate = ?; Greatest Decrease
# DecreaseProfit = ?

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    
    for row in csvreader:
        # add date
        date.append(row[0])
        
        # add profit/losses
        profit_losses.append(row[1])

        profit_losses[row] = int(profit_losses[row])
        
# set appropriate variables
total_months = len(date)
net_total = sum(profit_losses)

print(total_months)
print(net_total)

# see solution for wrestling with functions to see how to calculate and evaluate profit/losses as integers
#total_profloss = sum(profit_losses)
#print(total_profloss)
        # creating lists for each column
        #date variable doesn't seem to be working as a list, but as individual lines
        #date = row [0]
        #date_index = int(date) - doesn't work because it's not an integer
        #print(date_index)
        #profit_loss = row[1]
        
        #when going through rows, adds each row to list
        #total_months.append(date)
    
    # Loop through looking for the calculations to print; each row is a list; day 2 activity 12; day 3 activity 8
    #for row in csvreader:
        #if date == "":
            #print(date.index)
        
        # Total number of months included in the dataset (part of column 1); number of rows?; find index(number in list)
        # re-set TotalMonths to be next row, so that final is last row, but need to not count header row
        #print(date.index("Feb-17")) --> this didn't work
        
        # Net total amount of "Profit/Losses" (column 2) over the entire period; add them all up?
        
        # Average of the changes in "Profit/Losses" (column 2) over the entire period
        
        # Greatest increase in profits (date and amount) over the entire period
        
        # Greatest decrease in losses (date and amount) over the entire period
        
# Print final report as shown in example in homework instructions; will have to show as strings, not integers
#print(Financial Analysis)
#print("-----------------------------")
# Print total months
#print("Total Months: " + TotalMonths)
#print("Total: $" + NetTotal)
#print("Greatest Increase in Profits: " + IncreaseDate + "( $" + IncreaseProfit + ")")
#print("Greatest Decrease in Profits: " + DecreaseDate + " ($" + DecreaseProfit + ")") 

# Export text file with the final report (see day 2 activity 5, 11)
