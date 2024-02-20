 # William Beckham
 # 02-09-2024
 # P1HW1
 # Assignment tests student's knowledge of how to write code that collects information from user, processes information collected and display results to user.

#Use the input function to get an integer from the user. Assign the integer to a variable
#Print the integer, the square of the integer, and the cube of the integer, each on a separate line
#Use the input function to get another integer from the user. Assign it to a variable
#Print both integers separated by a plus sign and then the sum of the integers
#Print both integers separated by a multiplication sign and then the product of the integers
#The values should be able to change each time the program runs

user_num = int(input('Enter integer:\n')) 
print("You entered:", user_num)
print(user_num, "squared is", user_num ** 2)
print("And", user_num, "cubed is", user_num ** 3, "!!")
print('\n')

user_num2 = int(input('Enter another integer:\n'))
print("You entered:", user_num2)
print(user_num, "+", user_num2, "is", user_num2 + user_num)
print(user_num, "*", user_num2, "is", user_num2 * user_num)
