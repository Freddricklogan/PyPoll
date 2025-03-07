# PyPoll - Election Data Analysis
import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")

# Variables for analysis
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through rows
    for row in csvreader:
        # Count total votes
        total_votes += 1
        
        # Get candidate name
        candidate = row[2]
        
        # Add candidate to dictionary if not already there
        if candidate not in candidates:
            candidates[candidate] = 0
            
        # Increment candidate's vote count
        candidates[candidate] += 1

# Generate analysis report
analysis = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Calculate percentages and find the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    # Check if this candidate has the most votes
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

analysis += (
    f"-------------------------\n"
    f"Winner: {winner['name']}\n"
    f"-------------------------\n"
)

print(analysis)

# Export results to text file
output_path = os.path.join("analysis", "election_analysis.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(analysis)

print(f"Analysis exported to {output_path}")
