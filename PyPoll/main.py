import os
import csv


INPUT_CSV_PATH = os.path.join("Resources", "election_data.csv")
CANDIDATE_NAME_IDX = 2


Total_votes = 0
Candidate = []
Candidate_total_votes = []
Candidate_percent_votes = []
Winner = 0
# Create an empty dictionary to store the candidate names and vote counts
candidate_votes = {}

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(INPUT_CSV_PATH) as csv_file:
    # header=('voter_id','county', 'voter_name')
    reader = csv.reader(csv_file)
    next(reader)
    # Iterate through the list of votes
    for row in reader:
        # print(type(row), row)
        candidate_name = row[CANDIDATE_NAME_IDX]
        # Check if the candidate name is already in the dictionary
        if candidate_name in candidate_votes:
            # If yes, increment the vote count for that candidate
            candidate_votes[candidate_name] += 1
        else:
            # If no, add the candidate name to the dictionary with an initial vote count of 1
            candidate_votes[candidate_name] = 1

total_votes = sum(candidate_votes.values())

winner = max(candidate_votes, key=candidate_votes.get)

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
print(f"{candidate}: {candidate_percent_votes:.3f}% ({candidate_total_votes})\n")     
print("election results")
print(".......................")
print(f"total_votes: {total_votes}\n")
print(".......................")
for candidate_percent_votes in candidate:
    print(f"{candidate}: {candidate_percent_votes[candidate]:.3f}% ({candidate_total_votes[candidate]})")
print(".......................")
print(f"Winner: {Winner}\n")
print(".......................")

output_file = "output.txt"
with open(output_file, "w") as output_file:
    output_file.write("election results\n")
    output_file.write("......................\n")
    output_file.write(f"total_votes: {total_votes}\n")
    output_file.write(".......................\n")
    for candidate_percent_votes in candidate:
        output_file.write(f"{candidate}: {candidate_percent_votes[candidate]:.3f}% ({Candidate_total_votes[candidate]})")
    output_file.write(".......................\n")
    output_file.write(f"Winner: {Winner}\n")
    output_file.write(".......................\n")

