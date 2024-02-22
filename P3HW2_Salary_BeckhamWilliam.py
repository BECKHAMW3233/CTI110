# William Beckham
# 02-22-2024
# P3HW2
# Assignment assess student understanding of decision structures


# You are to create a program that does the following:
# Asks the user to enter name of employee
# Ask user to enter number of hours the employee worked this week
# Ask user to enter employee's pay rate
# Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
# Calculate amount employee should be paid for regular hours worked.
# Display gross pay (total amount that should be paid to employee)
# The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).

print()
name = input("Enter employee's name: ")
hrs_work = float(input('Enter numbers of hours worked: '))
rate = float(input("Enter employee's pay rate : "))

if hrs_work > 40:
    ot_hrs = hrs_work - 40
    ot_pay = ot_hrs * rate * 1.5
    reg_hrs = 40
    reg_pay = reg_hrs * rate
else:
    ot_hrs = 0
    ot_pay = 0
    reg_hours = hrs_work
    reg_pay = hrs_work * rate

gross = reg_pay + ot_pay

print('-------------------------------------')
print(f"{'Employee':<16} {name}")
print()
print(f"{'Hours Worked':<14} {'Pay Rate':<12} {'OverTime':<12} {'Overtime Pay':<20} {'RegHour Pay':<20} {'Gross Pay'}")
print('---------------------------------------------------------------------------------------------------')
print(f"{hrs_work:<14.2f} {rate:<12.2f} {ot_hrs:<12.2f} ${ot_pay:<20.2f} ${reg_pay:<20.2f} ${gross:.2f}")
print()