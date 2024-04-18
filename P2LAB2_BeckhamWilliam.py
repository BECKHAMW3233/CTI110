 # William Beckham
 # 02-15-2024
 # P2Lab2
 # Assignment tests student's knowledge of how to write code that displays information to users


num1 = float(input('Enter number here:\n'))
num2 = float(input('Enter number here:\n'))
num3 = float(input('Enter number here:\n'))
num4 = float(input('Enter number here:\n'))

your_value1 = num1 * num2 * num3 * num4 
your_value2 = ((num1 + num2 + num3 + num4) /4)
print()
print('-----------Results---------------')
print(f"{'Sum Multiplied: '} {your_value1:<10.0f} {'Average: '} {your_value2:.0f}")
print(f"{'Sum multiplied: '} {your_value1:<10.3f} {'Average: '} {your_value2:.3f}")