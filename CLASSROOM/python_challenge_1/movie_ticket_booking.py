'''Problem Statement 
Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage. '''
# --------------------------------------
# Movie Ticket Booking System
# Seat booking system

tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
}

# 1. Display available seats
print("Available Seats:")
for seat, status in tickets.items():
    if status == "Available":
        print(seat)

# 2. Count booked and available seats
booked = 0
available = 0

for status in tickets.values():
    if status == "Booked":
        booked += 1
    else:
        available += 1

print("\nBooked Seats:", booked)
print("Available Seats:", available)

# 3. Reserve first available seat
for seat, status in tickets.items():
    if status == "Available":
        tickets[seat] = "Booked"
        print("\nFirst available seat reserved:", seat)
        break

# 4. Save updated data to file
with open("tickets.txt", "w") as file:
    for seat, status in tickets.items():
        file.write(seat + " : " + status + "\n")

print("\nUpdated data saved to tickets.txt")

# 5. Calculate occupancy percentage
total_seats = len(tickets)
occupied = 0

for status in tickets.values():
    if status == "Booked":
        occupied += 1

occupancy = (occupied / total_seats) * 100

print("\nHall Occupancy:", occupancy, "%")