# Program to calculate Simple Interest

# Enter the values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Validate input
if principal < 0:
    exit("Principal cannot be negative.")
if rate < 0:
    exit("rate cannot be negative.")
if time < 0:
    exit("time cannot be negative.")

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest =", simple_interest) 