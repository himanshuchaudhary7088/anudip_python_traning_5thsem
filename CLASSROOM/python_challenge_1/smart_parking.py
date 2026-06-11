'''Problem Statement 
The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt. '''
#------------------------------------------------------------
# Smart Parking System
# Sample Data
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
]
# Function to display vacant parking slot numbers
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print("Vacant Slot: ",i + 1)
# Function to count occupied and vacant slots
occupied_count = 0
vacant_count = 0
for slot in parking_slots:
    if slot == "Occupied":
        occupied_count += 1
    else:
        vacant_count += 1
print("Occupied Slots: ", occupied_count)
print("Vacant Slots: ", vacant_count)
# Function to allocate the first vacant slot to a new vehicle
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("Allocated Slot: ", i + 1)
        break
# Function to calculate parking occupancy percentage
total_slots = len(parking_slots)
occupancy_percentage = (occupied_count / total_slots) * 100
print("Parking Occupancy Percentage: ", occupancy_percentage, "%")
# Function to store updated parking information in parking.txt
with open("parking.txt", "w") as file:
    for slot in parking_slots:
        file.write(slot + "\n")
print("Updated parking information saved to parking.txt")
