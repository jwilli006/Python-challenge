import os
import csv
#open CSV File
csvpath = os.path.join("Python", "PyBank_resources_budget_data.csv")

#path = os.path.dirname(os.path.realpath(__file__))
#csvpath1 = os.path.join(path, "raw_data", "budget_data_1.csv")
#Un-comment line below and comment out above line to test with 2nd data set
#csvpath1 = os.path.join(path, "raw_data", "budget_data_2.csv")

line = 0
months = []
total_revenue = 0
csv_dict =  {}
last_num = 0
change_dict = {}
total_change = 0 


with open(csvpath, newline="") as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=",")
    #SKIP HEADER
    csvreader1.__next__()

    for row in csvreader1:
        
        #CALCULATING TOTAL REVENUE
        total_revenue = total_revenue + int(row[1])
        
        #MAKE LIST OF MONTHS TO COUNT
        if row[0] not in months:
            months.append(row[0])
            #CALCULATE MONTHLY CHANGE
            change_dict[row[0]] = int(row[1]) - last_num
            last_num =  int(row[1])

  
for key, value in change_dict.items():
    #SKIP FIRST MONTH
    if key == months[0]:
        num = 0
    else:
        #CALCULATE TOTAL CHANGE FOR AVERAGE
        total_change = total_change + value
        

#FIND MONTHS OF MIN AND MAX CHANGES
min_price = min(zip(change_dict.values(), change_dict.keys()))
max_price = max(zip(change_dict.values(), change_dict.keys()))

min_change = (min_price[1] + " ($" + str(int(min_price[0]))+")")
max_change = (max_price[1] + " ($" + str(int(max_price[0]))+")")


total_revenue = "($" + str(int(total_revenue))+")"
num_months = len(months)
avg_change = "($" + str(int(total_change/(num_months - 1)))+")"

line = "-------------------------------"
results = (
    line +'\n' + "Financial Analysis" +'\n' + line +'\n'
    "Total Months: "+ str(num_months) +'\n'
    "Total Revenue: "+ str(total_revenue) +'\n'
    "Average Revenue Change: "+ str(avg_change) +'\n'
    "Greatest Increase in Revenue: "+ str(max_change) +'\n'
    "Greatest Decrease in Revenue: "+ str(min_change) +'\n' + line +'\n'
    )

print(results)

f = open("Financial_Analysis.txt", "w")

f.write(results)

f.close()