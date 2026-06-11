'''Problem Statement: Area of a Triangle Using Three Sides with Exception Handling 
Design a Python program to calculate the area of a triangle using Heron's Formula. The program should 
accept the lengths of the three sides of the triangle from the user and display the calculated area. 
However, the program must handle the following exceptional situations gracefully: 
1. If the user enters a non-numeric value instead of a number for any side, display an appropriate error 
message.  
2. If any of the entered side lengths are zero or negative, inform the user that triangle sides must be 
greater than zero.  
3. If the three entered side lengths cannot form a valid triangle according to the Triangle Inequality 
Theorem, notify the user that the triangle is invalid.  
4. Ensure that the program does not terminate abruptly due to invalid input and provides meaningful 
feedback using exception handling.  
5. Display a message indicating that the triangle area calculation process has been completed, 
regardless of whether the calculation was successful or an exception occurred.  
Note: Use Heron's Formula to calculate the area of the triangle: 
𝑠=(𝑎+𝑏+𝑐)/2
Area = √(s(s-a)(s-b)(s-c))'''
#----------------------------------------------------------
# Area of Triangle Using Three Sides with Exception Handling
try:
    a = float(input("Enter side a: "))
    if a <= 0:
        print("Error: Triangle sides must be greater than zero.")
        exit()
    b = float(input("Enter side b: "))
    if b <= 0:
        print("Error: Triangle sides must be greater than zero.")
        exit()
    c = float(input("Enter side c: "))
    if c <= 0:
        print("Error: Triangle sides must be greater than zero.")
        exit()
    
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Error: Invalid triangle (Triangle Inequality failed).")

    else:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"Area of triangle: {area:.4f}")

except ValueError:
    print("Error: Please enter numeric values only.")

finally:
    print("Triangle area calculation process completed.")