#program to perform various operations on a rectangle using a class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    #method to calculate area of the rectangle
    def area(self):
        print("Area of the rectangle:", self.length * self.breadth)
    #method to calculate perimeter of the rectangle
    def perimeter(self):
        print("Perimeter of the rectangle:", 2 * (self.length + self.breadth))
    #method to display the dimensions of the rectangle
    def display_dimensions(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
    #----------------------------------------------------
    # ask the user to enter the dimensions of the rectangle
length = float(input("Enter the length of the rectangle: "))
if length <= 0:
    print("Length must be greater than zero.")
    exit()
breadth = float(input("Enter the breadth of the rectangle: "))
if breadth <= 0:
    print("Breadth must be greater than zero.")
    exit()

# create an object of the Rectangle class
rectangle = Rectangle(length, breadth)
#menu-driven program to perform various operations on the rectangle
while True:
    print("\n_________rectangle operations_________:")
    print("1. Display dimensions")
    print("2. Calculate area")
    print("3. Calculate perimeter")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        rectangle.display_dimensions()
    elif choice == 2:
        rectangle.area()
    elif choice == 3:
        rectangle.perimeter()
    elif choice == 4:
        print("Thank you for using our services!")
        break
    else:
        print("Invalid choice! Please try again.")
# ask the user if they want to perform another operation
    another_operation = input("Do you want to perform another operation? (y/n): ")
    if another_operation.lower() != 'y':
        print("Thank you for using our services!")
        break        