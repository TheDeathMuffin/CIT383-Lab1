# Written by Samuel Long on September 4th, 2021 for the project "Lab 1" for the course CIT383.

# This program calculates the average number of hours each student spends studying for two subjects (Math and
# Scripting). The program inputs the number of students and the number of days in a long week. For each student on each
# day, the number of hours they spend on Math and Scripting is added to a list. After all students' information is
# gathered, the list is deconstructed using pop() while summing and averaging the hours spent by each student for the
# output.

while True:                                 # Loop continues until broken.
    students = int(input("Enter the number of students in the class (cannot be below 1): "))            # Input number of students.
    if students < 1:                        # If student number is less than one, continue looping.
        continue
    else:                                   # If student number is greater than one, move to input number of days.
        while True:                         # Loop continues until broken.
            days = int(input("Enter the number of days in a long week (must be between 1 and 7): "))    # Input number of days.
            if 1 <= days <= 7:              # If days are between 1 and 7, break. Other values will continue the loop.
                break           # Exit nested loop.
        break                   # Exit loop.

hourList = []                   # List for holding student hours.
for b in range(1, students + 1):            # Loops once for each student.
    for a in range(1, days + 1):            # Loops once for each day.
        while True:                         # Loop continues until broken.
            hours = float(input("Day " + str(a) + ", Student " + str(b) + ": Hours spent on Scripting (between 0 and 9): "))            # Input hours spent on Scripting.
            if 0 <= hours <= 9:             # If Scripting hours are between 0 and 9, break. Other values will continue the loop.
                break
        hourList.append(hours)              # Add Scripting hours to the list.
        while True:                         # Loop continues until broken.
            hours = float(input("Day " + str(a) + ", Student " + str(b) + ": Hours spent Math (between 0 and 9): "))                    # Input hours spent on Math.
            if 0 <= hours <= 9:             # If Math hours are between 0 and 9, break. Other values will continue the loop.
                break
        hourList.append(hours)              # Add Math hours to the list.

print("\n Student         Avg. Scripting Time      Avg. Math Time      Most Time Spent")                # Output labels.
print(" -------         -------------------      --------------      ---------------")

overallMath = 0                 # Initialized to 0, will hold sum of hours all students spend on Math.
overallScripting = 0            # Initialized to 0, will hold sum of hours all students spend on Scripting.

for j in range(1, students + 1):            # Loops once for each student.
    sumStudentMath = 0                      # Initialized to 0, will hold sum of hours a student spends on Math.
    sumStudentScripting = 0                 # Initialized to 0, will hold sum of hours a student spends on Scripting.
    for i in range(1, days + 1):            # Loops once for each day.
        sumStudentScripting = sumStudentScripting + hourList.pop(0)         # Adds Scripting hours for current day to student's Scripting sum by removing the first element from the list.
        sumStudentMath = sumStudentMath + hourList.pop(0)                   # Adds Math hours for current day to student's Math sum by removing the first element from the list.
    overallScripting = overallScripting + sumStudentScripting               # Adds student's overall Scripting sum to the overall Scripting sum.
    overallMath = overallMath + sumStudentMath                              # Adds student's overall Math sum to the overall Math sum.
    if sumStudentMath > sumStudentScripting:                # If student's Math sum > Scripting sum, most time spent is Math.
        mostTime = "Math"
    elif sumStudentMath < sumStudentScripting:              # If student's Math sum < Scripting sum, most time is Scripting.
        mostTime = "Scripting"
    else:                                                   # Otherwise, the same amount of time is spent.
        mostTime = "Same"
    print("{:>5} {:>22.2f} {:>22.2f}           {}".format(j, sumStudentScripting/days, sumStudentMath/days, mostTime))                  # Output student's data.

if overallMath > overallScripting:                      # If overall Math sum > overall Scripting sum, most time is Math.
    mostTime = "Math"
elif overallMath < overallScripting:                    # If overall Math sum < overall Scripting sum, most time is Scripting.
    mostTime = "Scripting"
else:                                                   # Otherwise, the same amount of time is spent.
    mostTime = "Same"
print(" -------         -------------------      --------------      ---------------")
print("Overall Avg. {:>15.2f} {:>22.2f}           {}".format(overallScripting/(days*students), overallMath/(days*students), mostTime))  # Output overall data.


# Sample Input:
# 3 2 9 6 7.5 6 7 9 9 7 8 6 5 8

# Output:
#  Student         Avg. Scripting Time      Avg. Math Time      Most Time Spent
#  -------         -------------------      --------------      ---------------
#     1                   8.25                   6.00           Scripting
#     2                   8.00                   8.00           Same
#     3                   6.50                   7.00           Math
#  -------         -------------------      --------------      ---------------
# Overall Avg.            7.58                   7.00           Scripting
