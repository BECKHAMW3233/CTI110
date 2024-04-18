# William Beckham
# 02-20-2024
# P2LAB
# Write a program that takes in a year and determines whether that year is a leap year




year = int(input('Give a year:\n'))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} - leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} - leap year".format(year))
else:
    print("{0} - not a leap year".format(year))