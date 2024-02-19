#William Beckham
#02.19.2024
#P2HW2
#Assignment assess student understanding of Lists



grades=[]
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))
print('\n')


print('-------------Results------------')
print(f"{'Lowest grade:':<20} {min(grades)}")
print(f"{'Highest grade:':<20} {max(grades)}")
print(f"{'Sum of grades:':<20} {sum(grades)}")
print(f"{'Average:':<20} {sum(grades) / len(grades):.2f}")
print('----------------------------------------')
