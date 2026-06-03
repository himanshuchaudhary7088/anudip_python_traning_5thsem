# Program to calculate Area and Perimeter of Rectangle

# Enter length and breadth
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

# Validate input
if length <= 0 or breadth <= 0:
    exit("Length and breadth must be greater than 0.")

# Calculate area
area = length * breadth

# Calculate perimeter
perimeter = 2 * (length + breadth)

# Display result
print("Area of Rectangle =", area, "sq.cm")
print("Perimeter of Rectangle =", perimeter, "cm")