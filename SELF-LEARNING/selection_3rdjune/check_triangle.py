# Enter and validate first side
side1 = float(input("Enter first side: "))
if side1 <= 0:
    exit("First side must be greater than 0")

# Enter and validate second side
side2 = float(input("Enter second side: "))
if side2 <= 0:
    exit("Second side must be greater than 0")

# Enter and validate third side
side3 = float(input("Enter third side: "))
if side3 <= 0:
    exit("Third side must be greater than 0")

# Verify triangle formation
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
       print("Triangle can be formed")
#triangle formed 
# type of triangle 
# isosceles triangle
       if(side1 == side2 or side2 == side3 or side1 == side3):
        print("triangle is sosceles triangle")
#Scalene Triangle
       elif(side1 == side2 or side2 == side3 or side1 == side3):
         print("triangle is Scalene Triangle")  
       else:
           print("triangle is equiletral")
else:
    print("Triangle cannot be formed") 