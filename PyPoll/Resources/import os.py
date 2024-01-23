import os
import csv
with open('\C:\Users\samka\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources', 'r') as file:
    lines = file.readlines()

    lines = line[1:]

    Total_votes = 0
    Candidate = []
    Candidate_total_votes = []
    Candidate_percent_votes = []
    Winner = 0

with open('\Users\samka\OneDrive\Documents\GitHub\python-challenge\PyBank\main.py', 'r') as file:
    lines = file.readlines()
    lines = lines[1:]
    for line in lines:
     data = [dict(zip(header,line.strip().split(',')))for line in lines [1:]

# Create an empty dictionary to store the candidate names and vote counts
candidate_votes = {}

# Iterate through the list of votes
for vote in votes:
    # Check if the candidate name is already in the dictionary
    if vote in candidate_votes:
        # If yes, increment the vote count for that candidate
        candidate_votes[vote] += 1
    else:
        # If no, add the candidate name to the dictionary with an initial vote count of 1
        candidate_votes[vote] = 1

total_votes = sum(candidates_votes.value())

candidate_percentages = {}

# Print the total votes for each candidate
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes} votes")
             
print("election results")
print(".......................")
print(f"total_votes: {total_votes}\n")
print(".......................")
for candidate in candidates:
    print(f{candidate}: {candidate_percent_votes[candidate]:.3f}% ({Candidate_total_votes[candidate]}))
print(".......................")
print(f"Winner: {Winner}\n")
print(".......................")

with open(output_file, "w") as output_file:
    output_file.write("election results\n")
    output_file.write("......................\n")
    output_file.write(f"total_votes: {total_votes}\n")
    output_file.write(".......................\n")
    for candidate in candidates:
        output_file.write(f{candidate}: {candidate_percent_votes[candidate]:.3f}% ({Candidate_total_votes[candidate]}))
    output_file.write(".......................\n")
    output_file.write(f"Winner: {Winner}\n")
    output_file.write(".......................\n")



             
                                                                         
                                                                        



    

