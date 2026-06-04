#A customer is adding items to a shopping cart. The price of each item is entered one by one. Write a program that continuously accepts item prices and calculates the total bill amount. The program should stop accepting prices when the user enters 0.
# Program to calculate total shopping bill

price = 1
total_bill = 0

# Loop runs until user enters 0
while price != 0:

    price = float(input("Enter item price (0 to stop): "))

    total_bill = total_bill + price

print("Total Bill Amount =", total_bill)