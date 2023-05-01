# CTI-110
# P3HW2 - Salary
# Willie Lockett
# 4/19/2023
# This progam is used to create and calculate Salary

Emp_name = (input('Enter the First and Last name:\n'))
Emp_hours = int(input('Enter the amount of hours worked:\n'))
Emp_rate = float(input('Enter the Rate of pay:\n'))
Overtime = Emp_hours-40
Overtime_pay = Emp_rate*(1.5*(Emp_hours-40))
gross_pay = (Overtime_pay + Emp_rate*Emp_hours)
#
print ( "---------------------------------------------------------- ")
print ('Employee name:', Emp_name)
print 
#def salary(pay):
if Emp_hours<=40:
    salary=Emp_rate*Emp_hours
elif Emp_hours>40:
    salary=Emp_rate*(1.5*(Emp_hours-40))
#return salary
print ('Hours Worked    Pay Rate     Overtime  Overtime Pay      Regular Pay       Gross Pay')
print ( "---------------------------------------------------------------------------------- ")
print (Emp_hours,  '            ', Emp_rate, '       ',Overtime,  '       ', Overtime_pay, "        ", salary, "           ", gross_pay)
