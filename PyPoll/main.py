import os
import csv

#set path
csvpath = os.path.join("..","PyPoll","Resources", 'election_data.csv')

#initialize
total_votes = 0
candidates_dict = {} #candidate name : vote count
percentage_dict = {} #candidate name : vote percentage
max_percent = 0
winner = ""
cand_data = ""
analysis = ""
#open csv file
with open (csvpath,'r',encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_file)
    #loop through rows
    for row in csv_reader:
        candidate_name = row[2]
        total_votes += 1
        #find unique candidate names
        if candidate_name not in candidates_dict:
            candidates_dict[candidate_name] = 1 # initialize name = 1 vote
        else:
            candidates_dict[candidate_name] += 1 # increase vote count
    #loop through dictionary   
    for candidate_name in candidates_dict:
        #calculate percent
        vote_percent = (candidates_dict[candidate_name] / total_votes) * 100
        percentage_dict[candidate_name] = vote_percent
        
        #find winner (max vote percent)
        if vote_percent > max_percent:
            max_percent = vote_percent
            winner = candidate_name
        cand_data += f'{candidate_name} : {vote_percent:.3f}% ({candidates_dict[candidate_name]})\n'


#Print analysis in Terminal
analysis+="\nElection Results\n"
analysis+="---------------------------\n"
analysis+=f"Total Votes: {total_votes}\n"
analysis+="---------------------------\n"
analysis+=cand_data
analysis+="---------------------------\n"
analysis+=f"Winnder: {winner}\n"
analysis+="---------------------------\n"
print(analysis)

#Print analysis in textfile
txt = '../PyPoll/Analysis/Output.txt'

with open(txt, 'w') as textfile:
    textfile.writelines(analysis)
textfile.close()
