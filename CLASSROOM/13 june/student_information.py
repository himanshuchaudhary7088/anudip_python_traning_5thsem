'''Student Information System (Basic) 
Problem Statement: 
Create a Student class to store the student's name, roll number, and marks obtained in three subjects. 
Implement methods to: 
• Accept student details.  
• Calculate the total marks.  
• Calculate the percentage.  
• Display the complete student report. '''
#program to implement a basic student information system using a class
class Student:
    def __init__(self, name, roll_number, marks1, marks2, marks3, max_marks):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.max_marks = max_marks    #maximum marks for each subject
    #method to calculate total marks
    def total_marks(self):
        print("total marks:", self.marks1 + self.marks2 + self.marks3)
    #method to calculate percentage
    def percentage(self):
        total = self.marks1 + self.marks2 + self.marks3
        percent = (total / (3 * self.max_marks)) * 100
        print("percentage:", percent , "%")
    #method to display complete student report
    def display_report(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks in Subject 1:", self.marks1)
        print("Marks in Subject 2:", self.marks2)
        print("Marks in Subject 3:", self.marks3)
        self.total_marks()
        self.percentage()
    #---------------------------------------------------    
    # main program to accept student details and display the report
name = input("Enter the student's name: ")
#to validate name input
if name.isspace():
    exit("Name cannot be empty.")
roll_number = int(input("Enter the student's roll number: "))
#to validate roll number input  
if roll_number<=0:
    exit("Roll number must be a positive integer.")
#maximum marks for each subject
max_marks = int(input("Enter the maximum marks for each subject: "))
#to validate maximum marks input
if max_marks <= 0:
    exit("Maximum marks must be greater than zero.")    
#------------------------------------------------------------------------------    
#marks obtained in three subjects
marks1 = float(input("Enter marks obtained in subject 1: "))
#to validate marks input
if marks1 < 0 or marks1 > max_marks:
    exit("Marks must be between 0 and maximum marks.")        
marks2 = float(input("Enter marks obtained in subject 2: "))
#to validate marks input
if marks2 < 0 or marks2 > max_marks:
    exit("Marks must be between 0 and maximum marks.")
marks3 = float(input("Enter marks obtained in subject 3: "))
#to validate marks input    
if marks3 < 0 or marks3 > max_marks:
    exit("Marks must be between 0 and maximum marks .")

# Create a Student object with the entered details
student = Student(name, roll_number, marks1, marks2, marks3, max_marks)

# Display the student report
student.display_report()