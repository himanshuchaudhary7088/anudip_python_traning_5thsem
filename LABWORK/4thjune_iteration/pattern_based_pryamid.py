# Program to print Number Pyramid

# Accept number of rows
rows = int(input("Enter number of rows: "))

# Print the pattern
for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end="")

    print()