#This line imports the csv module in Python, which provides functionality to work with CSV files 
import csv
#This initializes a variable to keep track of the total number of months in the dataset 
total_months = 0

#This line opens the file in read mode and assigns it to the variable file. The with statement ensures that the file properly closed after the block of code is executed 
with open('Resources/budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # next(csv_reader) 
    header = next(csv_reader)

    # for row in csv_reader:
    #     total_months += 1
    #     print(total_months)

    count_month = 0
    net_totalamount = 0
    amount_change = 0
    profit_loss_previous = 0
    greatest_increase = float('-inf')
    greatest_decrease = float('inf')
    greatest_increase_date = ""
    greatest_decrease_date = ""

    for row in csv_reader:
        count_month += 1
        net_totalamount += int(row[1])
        profit_loss_current = int(row[1])
        if count_month > 1:
            change = profit_loss_current - profit_loss_previous
            amount_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = row[0]
            profit_loss_previous = profit_loss_current
        average_change = amount_change / (count_month - 1) if count_month > 1 else 0
print("Total Months:", count_month)
print("Total: $" + str(net_totalamount))
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits:", greatest_increase_date, "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits:", greatest_decrease_date, "($" + str(greatest_decrease) + ")")
with open("output_file.txt", "w") as outputfile:
    outputfile.write("This is my output data")












