# CTI-110
# P4HW2 - Salary Calculator
# Willie Lockett
# 4/26/2023
###########################################################################
#Instructions:For assignment P4HW2, you will build on P3HW2 assignment. 
#The program however will calculate gross pay for multiple employees, 
#determined by user, and also calculates total amount paid for overtime, 
#total amount paid for regular pay and total amount paid for all employees.
############################################################################
# set global variables
numOfEmp = 0               # holds total employees entered
totalOverTimePay = 0       # holds total over time pay for all employees
totalRegPay = 0            # holds total regular pay for all employees
totalGrossPay = 0          # holds total gross pay for all employees

# now, run a loop until user wishes to exit
while True:
    
    # in each iteration, enter employee's name, hours worked, and pay rate
    name = input("Enter employee's name or \"None\" to terminate: ")
    
    # check if name is "None", then break the loop without any further user input
    if name == "None":
        break
    else:
        
        # if correct name then increase employee count by 1
        numOfEmp += 1
    
    hours = float(input("How many hours did " + name + " worked? "))
    rate = float(input("What did " + name + "\' pay rate? "))
    
    # variables to calculate values
    overtime = 0
    overtimePay = 0
    regularPay = 0
    grossPay = 0
    
    # check for overtime, if number of worked hours are greater than 40
    if hours > 40:
        
        # then calculate overtime
        overtime = hours - 40
        
        # calculate over time Pay(50% more)
        overtimePay = overtime * rate * 1.5
        
        # calculate regular pay
        regularPay = 40*rate
        
        # calculate gross Pay
        grossPay = regularPay + overtimePay
    else:
        
        # if no overtime is needed calculate regular Pay and gross pay
        regularPay = hours*rate
        grossPay = regularPay
    
    # compute total pay by adding over time pay to total over time pay
    totalOverTimePay += overtimePay
    
    # compute regular pay to total regular pay
    totalRegPay += regularPay
    
    # add gross pay to total gross pay
    totalGrossPay += grossPay
    
    # print employee name
    print("\nEmployee name: " + name + "\n")
    
    # print all the abover calculate values in tabular format as per the given format
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-------------------------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours, rate, overtime, overtimePay, regularPay, grossPay))
    print()

# print number of employees entered, total over time pay, total regular pay, and total gross pay
print()
print("Total number of employees entered:", numOfEmp)
print("Total amount payed for over time: $" + '{:.2f}'.format(totalOverTimePay))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(totalRegPay))
print("Total amount payed in gross: $" + '{:.2f}'.format(totalGrossPay))
