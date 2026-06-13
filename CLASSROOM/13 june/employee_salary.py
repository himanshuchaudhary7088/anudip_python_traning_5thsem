'''Employee Salary Management (Intermediate) 
Problem Statement: 
Create an Employee class containing employee ID, name, and monthly salary. 
Implement methods to: 
• Display employee details.  
• Calculate annual salary.  
• Increase salary by a given percentage. '''
#program to implement an employee salary management system using a class
class Employee:
    def __init__(self, emp_id, name, monthly_salary):
        self.emp_id = emp_id
        self.name = name
        self.monthly_salary = monthly_salary
    #method to display employee details
    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Monthly Salary: Rs.", self.monthly_salary)
    #method to calculate annual salary
    def annual_salary(self):
        print("Annual Salary: Rs.", self.monthly_salary * 12)
    #method to increase salary by a given percentage
    def increase_salary(self, percentage):
        if percentage < 0:
            exit("Percentage must be a positive value.")
        increase_amount = (self.monthly_salary * percentage) / 100
        self.monthly_salary += increase_amount
        print("updated Salary : Rs.", self.monthly_salary)
#---------------------------------------------------
# main program to accept employee details and perform operations
emp_id = input("Enter employee ID: ")
#to validate employee ID input
if emp_id.isalnum() == False:
    exit("Employee ID must be alphanumeric.")
name = input("Enter employee name: ")
#to validate name input
if not name.strip():
    exit("Name cannot be empty.")
#check if name contains only letters and spaces
if not all(ch.isalpha() or ch.isspace() for ch in name):
    exit("Name should contain only letters and spaces.")
monthly_salary = float(input("Enter monthly salary: "))
#to validate monthly salary input
if monthly_salary < 0:
    exit("Monthly salary must be a positive value.")

# Create an Employee object with the entered details
employee = Employee(emp_id, name, monthly_salary)
print("-----------employee details-----------")
# Display employee details
employee.display_details()

# Calculate and display annual salary
employee.annual_salary()

# Increase salary by a given percentage
percentage = float(input("Enter the percentage by which to increase the salary: "))
employee.increase_salary(percentage)