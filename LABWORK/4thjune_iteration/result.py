# Program to calculate Total Marks, Percentage, Grade
# and Number of Failed Subjects

# Accept marks of 5 subjects
sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))
sub4 = int(input("Enter marks of Subject 4: "))
sub5 = int(input("Enter marks of Subject 5: "))

# Calculate total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage
percentage = total / 5

# Count failed subjects
failed_subjects = 0

if sub1 < 40:
    failed_subjects = failed_subjects + 1

if sub2 < 40:
    failed_subjects = failed_subjects + 1

if sub3 < 40:
    failed_subjects = failed_subjects + 1

if sub4 < 40:
    failed_subjects = failed_subjects + 1

if sub5 < 40:
    failed_subjects = failed_subjects + 1

# Determine grade
if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"

# Display results
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Number of Subjects Failed =", failed_subjects)