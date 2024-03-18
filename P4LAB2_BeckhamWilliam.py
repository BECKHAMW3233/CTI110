# William Beckham
# P4LAB1
# 0305-2024
# Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second intege


num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number great than the first number:"))


if num1 <= num2:
    while num1 <= num2:
        print(num1, end=' ')
        num1 += 5
    print()
else:
    print('Second integer can\'t be less than the first.')