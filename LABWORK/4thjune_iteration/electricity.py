# Program to calculate Electricity Bill

# Accept units consumed from the user
units = int(input("Enter units consumed: "))

# Calculate bill according to slab rates
if units <= 100:
    bill = units * 5
    category = "Low Consumption"

elif units <= 200:
    bill = units * 7
    category = "Medium Consumption"

else:
    bill = units * 10
    category = "High Consumption"

# Display results
print("Units Consumed =", units)
print("Total Bill = Rs.", bill)
print("Category =", category)