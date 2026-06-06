#Employee Performance Evaluation 
'''....................................................................... 
Tasks 
Write a Python program to: 
1. Display details of employees scoring 80 or above.  
2. Count the number of employees who need improvement (score below 60).  
3. Find the employee with the highest score.  
4. Create a list containing the names of all employees scoring above 75.  
5. Display the performance category for each employee:  
o 90 and above → Excellent  
o 75 to 89 → Good  
o 60 to 74 → Average  
o Below 60 → Needs Improvement
..................................................................................'''

#Each employee record contains: 
employees = ( 
    ("E101", "Anuj", 92), 
    ("E102", "Rahul", 76), 
    ("E103", "Priya", 58), 
    ("E104", "Neha", 88), 
    ("E105", "Amit", 45) 
) 
# --------------------------------------------------
# 1. Display details of employees scoring 80 or above
print("Employees scoring 80 or above:")
for emp in employees:
    if emp[2] >= 80:
        print("ID:", emp[0], "Name:", emp[1], "Score:", emp[2])

# --------------------------------------------------
# 2. Count employees who need improvement (score below 60)
improvement_count = 0

for emp in employees:
    if emp[2] < 60:
        improvement_count += 1

print("\nEmployees needing improvement:", improvement_count)

# --------------------------------------------------
# 3. Find employee with highest score
highest_emp = employees[0]

for emp in employees:
    if emp[2] > highest_emp[2]:
        highest_emp = emp

print("\nEmployee with Highest Score:")
print("ID:", highest_emp[0])
print("Name:", highest_emp[1])
print("Score:", highest_emp[2])

# --------------------------------------------------
# 4. Create a list of names scoring above 75
high_performers = []

for emp in employees:
    if emp[2] > 75:
        high_performers.append(emp[1])

print("\nEmployees scoring above 75:")
print(high_performers)

# --------------------------------------------------
# 5. Display performance category for each employee
print("\nPerformance Categories:")

for emp in employees:
    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)

