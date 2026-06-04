 #A student must score at least 40 marks to pass an online assessment. The system allows the student to reattempt the test until the passing score is achieved. 
 #Write a program that accepts marks from the user and continues asking for marks until the entered score is 40 or more.Display a congratulatory message once the student passes the assessment.
# Program for Online Exam Portal

# Take marks from the student
marks = int(input("Enter your marks: "))

# Keep asking until marks are 40 or more
while marks < 40:
    print("You have not passed. Try again.")
    marks = int(input("Enter your marks: "))

# Display success message
print("Congratulations! You have passed the assessment.")