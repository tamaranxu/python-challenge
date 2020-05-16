# Modules
import os
import csv

# Set path for file
csvpath = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv"

# TotalMonths = ?; Total number of months included in the dataset; number of rows; try count() or len() function
# NetTotal = ?; Net total amount of Profit/Losses
# AvgChange = ?; Average Change; print(average(profit_losses)); define average as function
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
    #print(f"CSV Header: {csv_header}")
    
    #total number of rows; didn't work when under loop, but works here
    #look at House of Pies bonus code
    total_months = []    
    
    for row in csvreader:
        # creating lists for each column
        #date variable doesn't seem to be working as a list, but as individual lines
        date = row [0]
        #date_index = int(date) - doesn't work because it's not an integer
        #print(date_index)
        profit_loss = row[1]
        
        #when going through rows, adds each row to list
        total_months.append(date)
        
        #printed index for all rows, with last line being 86, which is correct and takes out header line
        print(str(len(total_months)))
        #print(len(total_months))
        #total_months = [str(len(date))
        #print(total_months)
        #print(profit_loss)
        #print(f"[{date.index(row)}] {date}") - didn't work'
        #for index, date in csvreader:  - just printed all values, no index numbers
            #print(index, date)
        #for i in range(len(date)):
            #print("[" + str(i) + "]" + date[i]) - printed each character in the date column, not whole value
    
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
        
# Print final report as shown in example in homework instructions
#print(Financial Analysis)
#print("-----------------------------")
# Print total months
#print("Total Months: " + TotalMonths)
#print("Total: $" + NetTotal)
#print("Greatest Increase in Profits: " + IncreaseDate + "( $" + IncreaseProfit + ")")
#print("Greatest Decrease in Profits: " + DecreaseDate + " ($" + DecreaseProfit + ")") 

# Export text file with the final report (see day 2 activity 5, 11)
