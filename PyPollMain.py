import os
import csv

# path to data file
csvpath = os.path.join("Python", "election_data.csv")

#variables
total_votes = 0
candidates_unique = []
candidate_vote_count = []

#read the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #This is the total votes cast, just count rows
        total_votes += 1
        #read in the candidate from column 3 of csv
        candidate_in = (row[2])
        #if candidate alreaady in list then locate the candidate by index # and increment the vote count by 1
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

#----------------------------------------------------
#QA the variables
#print(f'Total votes {total_votes}')
#print(f'Each candidate: {candidates_unique}')
#print(f'Index: {candidates_unique.index(candidate_in)}')
#----------------------------------------------------

pointcount = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    #calculation to get the percentage, x is the looper value
    vote_pointcount = round(candidate_vote_count[x]/total_votes*100, 2)
    pointcount.append(vote_pointcount)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

#----------------------------------------------------
#QA the variables
#print(f'Vote count for each candidate: {candidate_vote_count}')
#print(f'Max votes: {max_votes}')
#print(f'Election winner: {election_winner}')
#----------------------------------------------------

#To terminal
print('-------------------------------------------------------')
print('Election Results')
print('-------------------------------------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------------------------------------')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pointcount[x]}% ({candidate_vote_count[x]})')
print('-------------------------------------------------------')
print(f'Winner: {election_winner}\n')
print('-------------------------------------------------------')


#output txt file
with open('PyPoll_Election_Results.txt', 'w') as text:
    text.write('-----------------------------------------------\n')
    text.write('Election Results')
    text.write('-----------------------------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write('-----------------------------------------------\n')
    for x in range(len(candidates_unique)):
        text.write(f'{candidates_unique[x]} : {pointcount[x]}% ({candidate_vote_count[x]})\n')
    text.write('-----------------------------------------------\n')
    text.write(f'Winner: {election_winner}\n')
    text.write('-----------------------------------------------\n')
   
