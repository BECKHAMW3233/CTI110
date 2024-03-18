# William Beckham
# 03-07-2024
# P4HW1
# Assignment assess student ability to edit and enhance exiting programs


# Ask user to enter for number of scores they would like to enter. 
# Create a loop to collect the number of scores the user wants to enter.
# Note every time a score is entered, the following should be done
# Evaluate if the score is valid, it should be between 0 and 100 . 
# If it is not, notify the user and ask for a VALID score to be entered.
# Think of using another loop
# If score is valid, add the score to a list. Make sure the score list is given an informative name.
# After collecting all the scores. The program is to display the following:
# Lowest score entered
# Score List after dropping lowest score
# The average of scores in modified list
# Determine the letter grade for the calculated average and display it to user.


num_scores = int(input("How many scores do you want to enter? "))

scores = []
for i in range(num_scores):
   while True:
       try:
           score = float(input(f"Enter score #{i+1} : "))
           if 0 <= score <= 100:
               scores.append(score)
               break
           else:
               print()
               print("INVALID Score entered!!!")
               print('Score should be between 0 and 100')
       except ValueError:
           print("Invalid input. Please enter a numerical value.")

lowest_score = min(scores)
modified_scores = scores[1:]  # Create a new list without the lowest score

total_score = 0
for score in modified_scores:
   total_score += score

average = total_score / len(modified_scores)

if average >= 90:
   letter_grade = "A"
elif average >= 80:
   letter_grade = "B"
elif average >= 70:
   letter_grade = "C"
elif average >= 60:
   letter_grade = "D"
else:
   letter_grade = "F"

print("\n--------------Results-------------")
print(f"{'Lowest Score  :':<15} {lowest_score:.2f}")
print(f"{'Modified List :':<15} {modified_scores}")
print(f"{'Scores Average:':<15} {average:.2f}")
print(f"{'Grade         :':<15} {letter_grade}")
print("------------------------------------")