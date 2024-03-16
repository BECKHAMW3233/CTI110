# William Beckham
# 03-14-2024
# P5HW
# Write a program that gives simple math quizzes.

'''
Make the program a menu driven program. Meaning the program is to display a list of options to the user to choose from. List of options is shown below
 Add another function to the program that subtracts the generated random numbers. When program is executed, the MENU is to be displayed and user enters their choice. If user enters "1", the program is to add the numbers and asks user to guess what they add to. If "2" is entered, the program displays the numbers but asks enter the remainder of the subtraction and REMEMBER, program only terminates if user enters 3
    When/if user enters 1, the program is to execute a function that generates the numbers, adds them, asks user for enter an answer and display results.
    When/if user enters 2, the program is to execute a function that generates the numbers, subtracts them, asks user for enter an answer and display results.
    If/when the user enters 3, the program is to terminate.
    If/when user enters anything other than 1, 2, or 3, an error message should display letting the user know, then the menu should display again.
    When/if user guesses the right number, congratulate them and display the menu again to give them the option to play again
Program only terminates if user enters 3
'''

import random

def generate_problem(operation):
  num1 = random.randrange(1, 1000)
  num2 = random.randrange(1, 1000)
  if operation == "+":
    problem = str(num1) + " + " + str(num2)
    solution = num1 + num2
  elif operation == "-":
    problem = str(num1) + " - " + str(num2)
    solution = num1 - num2
  else:
    return "Invalid operation"
  return problem, solution

def main():
  while True:
    print("Choose an operation:")
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")

    if choice == "3":
      print()
      print("Thank you for playing...")
      print("Bye\n")
      break

    if choice not in ("1", "2"):
      print()
      print("Invalid choice. Please choose 1, 2, or 3.\n")
      continue

    operation = "+" if choice == "1" else "-"
    problem, solution = generate_problem(operation)
    print()

    attempts = 0  # Initialize attempts counter
    guessed_numbers = []  # List to store guessed numbers

    while True:
      print(problem)
      answer = input("Enter your answer (or 'q' to return to menu): \n")
      print()

      if answer.lower() == "q":
        break
      try:
        answer = int(answer)
        if answer == solution:
          attempts += 1  # Increment attempts only for correct answer
          print("Your answer was: ")
          print(answer)
          print("Congratulations!!!!!! Your Answer is Correct!\n")
          break
        elif answer > solution:
          attempts += 1  # Increment attempts
          print("Try again: ")
          print(answer)
          print("Your guess was a bit too high. Try again.\n")
        else:
          attempts += 1  # Increment attempts
          print("Try again: ")
          print(answer)
          print("Your guess was a bit too low. Try again.\n")
      except ValueError:
        print("Try again.")

    # Show attempted solutions and attempts only if the answer was correct
    if answer == solution:
      if guessed_numbers:  # Check if list is not empty before accessing elements
          print(f"You answered in {attempts} attempts.")
          print("Your attempted answers were: ", guessed_numbers)
    else:
      print(f"You attempted to answer {attempts} times, before you choose to quit.\n")  # Show attempts even when quitting with 'q'
      print("Your attempted answers were: ", guessed_numbers)
if __name__ == "__main__":
  main()
