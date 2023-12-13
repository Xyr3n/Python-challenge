#import modules
import os
import csv

#set path
csvpath = os.path.join("..","PyBank","Resources", 'budget_data.csv')

#initialize
total_months = 0
net_total = 0
start_amt = 0
prev_amt = 0
curr_amt = 0
curr_change = 0
avg_change = 0
max_inc = 0
max_dec = 0
#open the csv
with open (csvpath,'r',encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_file)
    
    #loop through rows
    for row in csv_reader:
        curr_amt = int(row[1])
        if total_months > 0:
            #find change in profit between each row
            curr_change = curr_amt - prev_amt
            #find the greatest increase in profit
            if curr_change > max_inc:
                max_inc = curr_change
                date_inc = row[0]
            #find the greatest decrease in profit
            if curr_change < max_dec:
                max_dec = curr_change
                date_dec = row[0]
        else:
            start_amt = curr_amt
        #calculate month, net total    
        total_months += 1
        net_total += curr_amt
        #set previous profit amount
        prev_amt = curr_amt
    #calculate change in profit and average change
    change_in_profit = curr_amt - start_amt
    avg_change = change_in_profit / (total_months - 1)
\

#Print analysis in Terminal
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {date_inc} (${max_inc})")
print(f"Greatest Decrease in Profits: {date_dec} (${max_dec})")


#Print analysis in textfile
txt = '../PyBank/Analysis/Output.txt'

with open(txt, 'w') as textfile:
    textfile.writelines("Financial Analysis\n")
    textfile.writelines("---------------------------\n")
    textfile.writelines(f"Total Months: {total_months}\n")
    textfile.writelines(f"Total: ${net_total}\n")
    textfile.writelines(f"Average Change: ${avg_change:.2f}\n")
    textfile.writelines(f"Greatest Increase in Profits: {date_inc} (${max_inc})\n")
    textfile.writelines(f"Greatest Decrease in Profits: {date_dec} (${max_dec})\n")
textfile.close()

   

