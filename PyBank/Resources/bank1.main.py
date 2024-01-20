import os
import csv


# Read the data from a CSV file
with open('budget_data.csv', 'r') as file:
    lines = file.readlines()

# Remove the header line
lines = lines[1:]

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_value = 0
changes = []
greatest_increase = 0
greatest_decrease = 0

# Loop through each line of data
for line in lines:
    # Split the line into date and profit/losses
    date, profit_losses = line.strip().split(',')

    # Convert profit/losses to an integer
    profit_losses = int(profit_losses)

    # Calculate the total profit/losses
    total_profit_losses += profit_losses

    # Calculate the change in profit/losses
    change = profit_losses - previous_value

    # Add the change to the list
    changes.append(change)

    # Update the previous value
    previous_value = profit_losses

    # Find the greatest increase and decrease
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_date = date
    if change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_date = date

    # Increment the total months
    total_months += 1

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the results
print("Financial Analysis")
print("-----------------------------")
print("Total Months:", total_months)
print("Total: $", total_profit_losses)
print("Average Change: $", average_change)
print("Greatest Increase in Profits:", greatest_increase_date, "($", greatest_increase, ")")
print("Greatest Decrease in Profits:", greatest_decrease_date, "($", greatest_decr 
    
