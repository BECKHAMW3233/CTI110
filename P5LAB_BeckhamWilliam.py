# William Beckham
# 03-14-2024
# P5LAB
# The function should return the number of days in February for the input year

def days_in_feb(user_year): 
    if user_year % 4 == 0 and user_year % 100 != 0: #Condition to check regular leap years 
        return 29
    elif user_year % 400 == 0:                      #Condition to check XX00s
        return 29
    else:                                           #Condition for non-leap years
        return 28

if __name__ == '__main__':
    year = int(input('Please enter a year.\n'))
    day = days_in_feb(int(year))
    print(f'{year} has {day} days in February.')