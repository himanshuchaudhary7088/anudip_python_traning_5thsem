# Program to simulate lift movement from floor 0

# Initial position of lift
current_floor = 0

# Total distance travelled
total_travelled = 0

while True:

    # Take destination input
    dest = int(input("Enter Destination Floor (-1 to stop): "))

    # Stop condition
    if dest == -1:
        break

    # Calculate floors travelled in this trip
    travelled = dest - current_floor

    # If moving down, convert to positive distance
    if travelled < 0:
        travelled = -travelled

    # Add to total travelled distance
    total_travelled = total_travelled + travelled

    # Update current floor
    current_floor = dest

    # Display travel for this trip
    print("Travelled:", travelled, "floors")

# Display total travel
print("Total Travelled:", total_travelled, "floors")