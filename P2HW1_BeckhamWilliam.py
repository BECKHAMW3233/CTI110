
# William Beckham
# 02-15-2024
# P2HW1
# Assignment assess student ability to edit and enhance exiting programs channges made to P1HW2, to affect alignment of data

# Ask user to enter their budget
# Ask user to enter travel destination
# Ask user for amount they will spend on gas
# Ask user for amount they will spend on accommodation
# Ask user for amount they will spend on food
# Add expenses
# Subtract expenses from budget
# Display results
# A dollar sign ($) must appear right before the amounts in the printout of travel expenses
# on printout of expenses the dollar ammounts should be aligned in a colum




budget = float(input('Enter budget here:\n'))
lodging = float(input('Enter lodging amount here:\n'))
fuel = float(input('Enter gas budget here:\n'))
food = float(input('Enter food budget here:\n'))
destination = input('Enter destination name:\n')
print("\n\n")
print("This program calculates and displays travel expenses", "\n")
print("Enter Budget:", budget, "\n")
print("Enter your travel destination:", destination, "\n")
print("How much do you think you will need spend on gas?", fuel, "\n")
print("Approximately, how will you need for accomodation/hotel?", lodging, "\n")
print("Last, how much do you need for food?", food, "\n")
print('------------Travel Expenses------------')
print(f"{'Location:':<19} {destination:}")
print(f"{'Initial Budget:':<19} ${budget:.2f}")
print(f"{'Fuel:':<19} ${fuel:.2f}")
print(f"{'Accomodation:':<19} ${lodging:.2f}")
print(f"{'Food:':<19} ${food:.2f}", "\n")
bal = budget - lodging - fuel - food
print(f"{'Remaining Balance:':<19} ${bal:.2f}")