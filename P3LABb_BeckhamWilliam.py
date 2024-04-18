# William Beckham
# 03-14-2024
# P3LABb
# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line.


amount_input = int(input('Enter a whole number no decimals:\n'))

dollars = amount_input // 100
quarters = amount_input % 100 // 25
dimes = amount_input % 100 % 25 // 10
nickels = amount_input % 100 % 25 % 10 // 5
pennies = amount_input % 100 % 25 % 10 % 5 // 1
print()
print('This is how many dollars and coins you need to equal this number.')
print('Using the least amount of coins and bills.')
if amount_input <= 0:
    print("No change")

if dollars > 1:
    print(str(dollars) + " Dollars")
elif dollars == 1:
    print(str(dollars) + " Dollar")
else:
    pass
if quarters > 1:
    print(str(quarters) + " Quarters")
elif quarters == 1:
    print(str(quarters) + " Quarter")
else:
    pass
if dimes > 1:
    print(str(dimes) + " Dimes")
elif dimes == 1:
    print(str(dimes) + " Dime")
else:
    pass
if nickels > 1:
    print(str(nickels) + " Nickels")
elif nickels == 1:
    print(str(nickels) + " Nickel")
else:
    pass
if pennies > 1:
    print(str(pennies) + " Pennies")
elif pennies == 1:
    print(str(pennies) + " Penny")