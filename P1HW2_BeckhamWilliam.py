 # William Beckham
 # 02-13-2024
 # P1HW2
 # For this assignment you will create a program that does some basic math on numbers that are entered


budget = int(input('Enter budget here:\n'))
lodging = int(input('Enter lodging amount here:\n'))
fuel = int(input('Enter gas budget here:\n'))
food = int(input('Enter food budget here:\n'))
destination = input('Enter destination name:\n')
print("\n\n")
print("This program calculates and displays travel expenses", "\n")
print("Enter Budget:", budget, "\n")
print("Enter your travel destination:", destination, "\n")
print("How much do you think you will need spend on gas?", fuel, "\n")
print("Approximately, how will you need for accomodation/hotel?", lodging, "\n")
print("Last, how much do you need for food?", food, "\n")
print('------------Travel Expenses------------')
print("Location:", destination)
print("Initial Budget:", budget, "\n")
print("Fuel", fuel)
print("Accomodation:", lodging)
print("Food", food, "\n")
print("Remaining Balance:", budget - lodging - fuel - food)