# Student Performance Analyzer

marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Passed students
passed_students = []

# Merit list (marks > 75)
merit_list = []

# Failed count
failed_count = 0

# Highest and Lowest initialization
highest = marks[0]
lowest = marks[0]

for i in marks:

    # Passed students
    if i >= 40:
        passed_students.append(i)
    else:
        failed_count += 1

    # Merit list
    if i > 75:
        merit_list.append(i)

    # Highest marks
    if i > highest:
        highest = i

    # Lowest marks
    if i < lowest:
        lowest = i

print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)