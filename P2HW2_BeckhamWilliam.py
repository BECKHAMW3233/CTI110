#William Beckham
#02.19.2024
#P2HW2
#Assignment assess student understanding of Lists

# Ask the user to enter grade for each module
# inputed grades should be in a saved list for later use
# Display the following:
    #The lowest grade in the list
    #The highest grade in the list
    #Sum of grades
    #The grades' average
# inputed grades should show 2 decimal places on printout of grades

grades=[]
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))
print('\n')


print('-------------Results------------')
print(f"{'Lowest grade:':<20} {min(grades):.2f}")
print(f"{'Highest grade:':<20} {max(grades):.2f}")
print(f"{'Sum of grades:':<20} {sum(grades):.2f}")
print(f"{'Average:':<20} {sum(grades) / len(grades):.2f}")
print('----------------------------------------')