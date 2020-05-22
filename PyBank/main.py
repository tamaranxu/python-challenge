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

    # Set start value for previous row, increase, decrease variables
    previous_row = 0
    greatest_increase = 0
    greatest_decrease = 0
    
    for row in csvreader:
                
        # add date column to list
        date.append(row[0])
        
        # add profit_losses column to list as integer
        profit_losses.append(int(row[1]))
        
        # variable for change
        change = int(row[1]) - int(previous_row)
        
        # calculate difference between profit_losses column and previous row; add to list as integer
        if previous_row == 0:
            #set first value as 0, since no previous row
            changes.append(int(0))
        else:
            changes.append(change)
            
            # calculate largest increase number and identify corresponding date
            if change >= greatest_increase:
                greatest_increase = change
                date_grt_incr = row[0]
            
            # calculate largest decrease number and identify corresponding date
            elif change <= greatest_decrease:
                greatest_decrease = change
                date_grt_decr = row[0]
        
        #re-set value of previous row
        previous_row = int(row[1])
        
# find total number of months in data set
total_months = len(date)

# find the net total of profit/losses over entire period
net_total = sum(profit_losses)

# find average of changes in profit/losses over entire period, excluding first row (rounded to 2 decimals)
average_change = round(sum(changes)/(len(changes)-1), 2)

# print results
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {str(date_grt_incr)} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {str(date_grt_decr)} (${str(greatest_decrease)})")

# export text file with same results
# set variable for output file
output_file = r"C:\Users\tamar\OneDrive\Documents\GitHub\python-challenge\PyBank\Analysis\bank_results.csv"

# Open the output file
# newline="" is used to take out space in between rows
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the results; add brackets to keep comma from separating characters in string
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------------"])
    writer.writerow([f"Total Months: {str(total_months)}"])
    writer.writerow([f"Total: ${str(net_total)}"])
    writer.writerow([f"Average Change: ${str(average_change)}"])
    writer.writerow([f"Greatest Increase in Profits: {str(date_grt_incr)} (${str(greatest_increase)})"])
    writer.writerow([f"Greatest Decrease in Profits: {str(date_grt_decr)} (${str(greatest_decrease)})"])