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
# Smart Railway Reservation System
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

    #check the available seats
print("Available Seats:", [seat for seat, status in seats.items() if status == "Available"])
#count booked and available seats

booked_count = sum(1 for status in seats.values() if status == "Booked")
available_count = sum(1 for status in seats.values() if status == "Available")
print(f"Booked Seats: {booked_count}, Available Seats: {available_count}")
#reserve the first available seat
for seat, status in seats.items():
    if status == "Available":
        seats[seat] = "Booked"
        print(f"Seat {seat} reserved.")
        break
   

#cancel booking for a given seat number
seat_number = int(input("Enter Seat Number to Cancel Booking: "))
if seat_number in seats and seats[seat_number] == "Booked":
    seats[seat_number] = "Available"
    print(f"Booking for Seat {seat_number} cancelled.")
else:
        print("Invalid seat number or seat is not booked.")
#store the updated reservation status in reservations.txt
with open("reservations.txt", "w") as f:
    for seat, status in seats.items():
     f.write(f"Seat {seat}: {status}\n")
     print("Updated reservation status stored in reservations.txt.")
#display occupancy percentage
total_seats = len(seats)
booked_seats = sum(1 for status in seats.values() if status == "Booked")
occupancy_percentage = (booked_seats / total_seats) * 100 if total_seats > 0 else 0
print(f"Occupancy Percentage: {occupancy_percentage:.2f}%")
print("Reservation Details Saved Successfully.")