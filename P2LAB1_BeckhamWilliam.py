 # William Beckham
 # 02-15-2024
 # P2LAB1
 # Assignment tests student's knowledge of how to write code that performs mathematical calculations and displays information to users



miles_per_gallon=float(input('Enter miles per gallon:\n'))
dollars_per_gallon=float(input('Enter price per gallon of gas:\n'))
print('\n')
dollars_per_mile = dollars_per_gallon/miles_per_gallon
your_value1 = 20 * dollars_per_mile
your_value2 = 75 * dollars_per_mile
your_value3 = 500 * dollars_per_mile
print('---------Miles Traveled------------')
print(f"{'20 miles':<10} {'75 miles':<10} {'500 miles'}")
print(f'${your_value1:<9.2f} ${your_value2:<9.2f} ${your_value3:.2f}')