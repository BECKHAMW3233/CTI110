# William Beckham
# 03-14-2024
# P4HW2
# For assignment P4HW2, you will build on P3HW2 assignment. The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees


'''
Asks the user employee name
Enter user pay rate and hours worked
Calculate overpay and regular pay. Store these values in variables, at the end of the program you will display overtime total, regular pay total, gross pay total, and number of employees entered
Ask user to enter another employee's name to calculate salary for or "Done" to terminate program. Note we are using sentinels here.
When user chooses to stop entering employee information , display results as shown in image below.
THE PROGRAM ONLY TERMINATES IF THE USER ENTERS "Done" for employee name
'''


total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while True:
  print()
  name = input("Enter employee's name (or 'done' to quit): ")
  if name.lower() == 'done':
    print()
    break  # Exit the loop if user enters 'done'

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

  total_employees += 1
  total_overtime_pay += ot_pay
  total_regular_pay += reg_pay
  total_gross_pay += (ot_pay + reg_pay)

  print('-------------------------------------')
  print(f"{'Employee name:':<16} {name}")
  print()
  print(f"{'Hours Worked':<14} {'Pay Rate':<12} {'OverTime':<12} {'Overtime Pay':<20} {'RegHour Pay':<20} {'Gross Pay'}")
  print('---------------------------------------------------------------------------------------------------')
  print(f"{hrs_work:<14.2f} {rate:<12.2f} {ot_hrs:<12.2f} ${ot_pay:<19.2f} ${reg_pay:<20.2f} ${(reg_pay + ot_pay):.2f}")
  print()

print("Payroll Summary:")
print(f"{'Total number of Employees entered:':<38} {total_employees}")
print(f"{'Total amount paid for overtime:':<38} ${total_overtime_pay:.2f}")
print(f"{'Total amount paid for regular hours:':<38} ${total_regular_pay:.2f}")
print(f"{'Total amount paid in gross:':<38} ${total_gross_pay:.2f}")

