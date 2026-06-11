'''Problem Statement 
Student enrollment data for university courses is stored below. 
Sample Data 
enrollment = { 
    "Python": 45, 
    "Java": 38, 
    "Data Science": 52, 
    "Web Development": 34, 
    "Machine Learning": 41, 
    "Cloud Computing": 29, 
    "Cyber Security": 33, 
    "DBMS": 48, 
    "Networking": 26, 
    "Operating Systems": 37 
}
Tasks 
1. Display courses having more than 40 enrollments.  
2. Find the most and least popular courses.  
3. Calculate total enrollments.  
4. Create lists:  
o High Demand (>40)  
o Medium Demand (30–40)  
o Low Demand (<30)  
5. Count courses requiring promotional activities (<35 enrollments).   '''
#---------------------------------------------
#university course 
#sample data 
enrollment = { 
    "Python": 45, 
    "Java": 38, 
    "Data Science": 52, 
    "Web Development": 34, 
    "Machine Learning": 41, 
    "Cloud Computing": 29, 
    "Cyber Security": 33, 
    "DBMS": 48, 
    "Networking": 26, 
    "Operating Systems": 37 
}
#function to display courses having more than 40 enrollments
print("Courses with more than 40 enrollments:")
for course, count in enrollment.items():
    if count > 40:
        print(course)
#function to find the most and least popular courses
most_popular = enrollment["Python"]
least_popular = enrollment["Python"]
for count in enrollment.values():
    if count > most_popular:
        most_popular = count
    if count < least_popular:
        least_popular = count
print("\nMost Popular Course: ", most_popular, "enrollments")
print("Least Popular Course: ", least_popular, "enrollments")
#function to calculate total enrollments
total_enrollments = 0
for count in enrollment.values():
    total_enrollments += count
print("\nTotal Enrollments: ", total_enrollments)
#function to create lists based on demand
high_demand = []
medium_demand = []
low_demand = []
for course, count in enrollment.items():
    if count > 40:
        high_demand.append(course)
    elif 30 <= count <= 40:
        medium_demand.append(course)
    else:
        low_demand.append(course)
print("\nHigh Demand Courses: ", high_demand)
print("Medium Demand Courses: ", medium_demand)
print("Low Demand Courses: ", low_demand)
#function to count courses requiring promotional activities (<35 enrollments)
promotional_courses_count = 0
for count in enrollment.values():
    if count < 35:
        promotional_courses_count += 1
print("\nNumber of courses requiring promotional activities: ", promotional_courses_count)
