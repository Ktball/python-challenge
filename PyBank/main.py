import os
import csv


# Read the data from a CSV file
INPUT_CSV_PATH = os.path.join("Resources", "budget_data.csv")


# Initialize variables
total_months = 0
total_profit_losses = 0
previous_value = 0
changes = []
max_increase = 0
max_decrease = 0
date = []
profit_losses = []

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(INPUT_CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    # Split the line into date and profit/losses
    for row in csv_reader:
        date = row[0]
        profit_losses = int(row[1])

        total_months += 1
        total_profit_losses += profit_losses

    if total_months > 1:
        change = profit_losses - previous_value
        changes.append(change)

    # Find the greatest increase and decrease
    if change > max_increase:
        max_increase = change
        max_increase_date = date
    if change < max_decrease:
        max_decrease = change
        max_decrease_date = date

    previous_profit_loss = profit_losses 

# Calculate the average change
average_change = sum(changes) / (total_months-1)

# Print the results
print("Financial Analysis")
print("-----------------------------")
print("Total Months:", total_months)
print("Total: $", total_profit_losses)
print("Average Change: $", average_change)
print("Greatest Increase in Profits:", max_increase_date, "($", max_increase, ")\n")
print("Greatest Decrease in Profits:", max_decrease_date, "($", max_decrease,")\n")

output_file = "output.txt"
with open(output_file, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")