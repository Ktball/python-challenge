import os
import csv


# Read the data from a CSV file
with open('\Users\samka\OneDrive\Documents\GitHub\python-challenge\PyBank\main.py', 'r') as file:
    lines = file.readlines()

# Remove the header line
lines = lines[1:]

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_value = 0
changes = []
max_increase = 0
max_decrease = 0

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
    if change > max_increase:
        max_increase = change
        max_increase_date = date
    if change < max_decrease:
        max_decrease = change
        max_decrease_date = date

    # Increment the total months
    total_months += 1

# Calculate the average change
average_change = sum(changes) / (total_months-1)

# Print the results
print("Financial Analysis")
print("-----------------------------")
print("Total Months:", total_months)
print("Total: $", total_profit_losses)
print("Average Change: $", average_change)
print("Greatest Increase in Profits:", max_increase_date, "($", greatest_increase, ")")
print("Greatest Decrease in Profits:", max_decrease_date, "($", greatest_decrease,")")

print(output)

output_file = \Users\samka\OneDrive\Documents\GitHub\python-challenge\PyBank\analysis\result.txt
with open(output_file, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f'Average Change: ${average_change:.2f}')

