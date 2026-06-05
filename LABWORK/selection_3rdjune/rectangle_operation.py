# Program to calculate Area and Perimeter of Rectangle
# Enter length and breadth
length = float(input("Enter length of rectangle(in cm): "))
breadth = float(input("Enter breadth of rectangle(in cm): "))

# Validate input
if breadth <= 0:
    exit("breadth must be greater than 0.")
if length <= 0:
    exit("Length must be greater than 0.")

# Calculate area
area = length * breadth

# Calculate perimeter
perimeter = 2 * (length + breadth)

# Display result
print("Area of Rectangle =", area, "sq.cm")
print("Perimeter of Rectangle =", perimeter, "cm")