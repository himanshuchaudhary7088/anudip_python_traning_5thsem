#A flight reservation system stores passenger records as tuples: 
'''...............................................................
Write a Python program to: 
1. Display all passengers whose booking status is Confirmed.  
2. Count the number of passengers travelling to Delhi.  
3. Count Confirmed, Waiting, and Cancelled bookings separately.  
4. Create a list containing passenger IDs with Waiting status.  
5. Determine which destination has the highest number of bookings.  
.................................................................'''
# Flight Reservation System

bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# --------------------------------------------------
# 1. Display all confirmed passengers

print("Confirmed Passengers:")
for booking in bookings:
    if booking[2] == "Confirmed":
        print("Passenger ID:", booking[0],
              "Destination:", booking[1])

# --------------------------------------------------
# 2. Count passengers travelling to Delhi

delhi_count = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi_count = delhi_count + 1

print("\nPassengers travelling to Delhi:", delhi_count)

# --------------------------------------------------
# 3. Count Confirmed, Waiting and Cancelled bookings

confirmed = 0
waiting = 0
cancelled = 0

for booking in bookings:
    if booking[2] == "Confirmed":
        confirmed = confirmed + 1
    elif booking[2] == "Waiting":
        waiting = waiting + 1
    elif booking[2] == "Cancelled":
        cancelled = cancelled + 1

print("\nConfirmed Bookings:", confirmed)
print("Waiting Bookings:", waiting)
print("Cancelled Bookings:", cancelled)

# --------------------------------------------------
# 4. Create a list of passenger IDs with Waiting status

waiting_passengers = []

for booking in bookings:
    if booking[2] == "Waiting":
        waiting_passengers.append(booking[0])

print("\nWaiting Passenger IDs:")
print(waiting_passengers)

# --------------------------------------------------
# 5. Find destination with highest number of bookings

delhi = 0
mumbai = 0
chennai = 0

for booking in bookings:
    if booking[1] == "Delhi":
        delhi = delhi + 1
    elif booking[1] == "Mumbai":
        mumbai = mumbai + 1
    elif booking[1] == "Chennai":
        chennai = chennai + 1

highest_destination = "Delhi"
highest_count = delhi

if mumbai > highest_count:
    highest_destination = "Mumbai"
    highest_count = mumbai

if chennai > highest_count:
    highest_destination = "Chennai"
    highest_count = chennai

print("\nDestination with Highest Bookings:")
print(highest_destination, "-", highest_count)