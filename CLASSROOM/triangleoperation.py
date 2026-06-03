#program to calculate area and perimeter of triangle
#input of three sides
side1 = int(input("enter the first side of triangle(in cm) :"))
side2 = int(input("enter the second side of triangle(in cm) :"))
side3 = int(input("enter the first side of triangle(in cm) :"))
#........................................................................
print("--------------------------------------------")
print("first side is :",side1)
print("second side is :",side2)
print("third side is :",side3)
#to calculate the perimeter
perimeter = side1+side2+side3
print( "perimeter of triangle is :" , perimeter, "cm") 
#..........................................................................
#to calculate the area
s = perimeter/2
area =(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("area of the triangle is :",area ,"sq.cm")