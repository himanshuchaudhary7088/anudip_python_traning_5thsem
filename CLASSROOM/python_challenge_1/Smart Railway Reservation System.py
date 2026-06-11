'''Problem Statement 
A railway reservation system stores the booking status of seats in a train coach. 
Sample Data 
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage. '''
#------------------------------------------------------------
# Smart Railway Reservation System (Beginner Version)

# Step 1: Seat data (1 = seat number, value = status)
seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}

# Step 2: Show all available seats
print("Available Seats are:")

for seat in seats:
    if seats[seat] == "Available":
        print(seat, end=" ")

print()  # new line


# Step 3: Count booked and available seats
booked = 0
available = 0

for status in seats.values():
    if status == "Booked":
        booked += 1
    else:
        available += 1

print("Booked Seats:", booked)
print("Available Seats:", available)


# Step 4: Book first available seat
for seat in seats:
    if seats[seat] == "Available":
        seats[seat] = "Booked"
        print("Seat", seat, "has been reserved.")
        break


# Step 5: Cancel booking
seat_number = int(input("Enter seat number to cancel booking: "))

if seat_number in seats:
    if seats[seat_number] == "Booked":
        seats[seat_number] = "Available"
        print("Booking cancelled for seat", seat_number)
    else:
        print("This seat is already available.")
else:
    print("Invalid seat number.")


# Step 6: Save updated data to file
file = open("reservations.txt", "w")

for seat in seats:
    file.write("Seat " + str(seat) + ": " + seats[seat] + "\n")

file.close()
print("Updated data saved in reservations.txt")


# Step 7: Calculate occupancy percentage
total_seats = len(seats)
booked_count = 0

for status in seats.values():
    if status == "Booked":
        booked_count += 1

occupancy = (booked_count / total_seats) * 100

print("Occupancy Percentage:", round(occupancy, 2), "%")
print("System update completed.")