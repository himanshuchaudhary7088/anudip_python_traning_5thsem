#Problem Statement
#A bus has seats represented as:
#seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
#Where:
#• 1 → Seat Booked
#• 0 → Seat Available
#Write a program to:
#1. Count booked and available seats.
#3. Create a list of all available seat numbers.
#4. Determine whether the bus is more than 70% occupied. 

seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0
available_seats = []

# Count booked and available seats
for i in seats:
    if i == 1:
        booked = booked + 1
    else:
        available = available + 1

print("Booked Seats :", booked)
print("Available Seats :", available)

# Find first available seat
for i in range(len(seats)):
    if seats[i] == 0:
        print("First Available Seat Number :", i + 1)
        break

# Create list of all available seat numbers
for i in range(len(seats)):
    if seats[i] == 0:
        available_seats.append(i + 1)

print("Available Seat Numbers :", available_seats)

# Check occupancy percentage
occupancy = (booked / len(seats)) * 100

print("Occupancy Percentage :", occupancy, "%")

if occupancy > 70:
    print("Bus is more than 70% occupied")
else:
    print("Bus is not more than 70% occupied")