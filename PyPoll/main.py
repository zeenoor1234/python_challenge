import csv
total_votes = 0
candidates_list = []
candidate_votes = {}
with open('Resources/election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) #skip the header
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
print(f"Total Votes: {total_votes}")
print("List of Candidates who received votes:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes}")
for candidate in candidates_list:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
winner = max(candidate_votes, key=candidate_votes.get)
winning_votes = candidate_votes[winner]
print(f"Winner: {winner} with {winning_votes} votes")