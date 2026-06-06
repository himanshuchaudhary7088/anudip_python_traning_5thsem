#smart parking system
'''-------------------------------------
Write a program to: 
• Count occupied and available slots.  
• Find the first available slot.  
• Display all available slot numbers.  
• Check whether parking occupancy exceeds 75%.  
-----------------------------------------'''
#Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 

'''Where: 
• 1 = Occupied  
• 0 = Available '''
# ------------------------------------------
# Count occupied and available slots

occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied = occupied + 1
    else:
        available = available + 1

print("Occupied Slots :", occupied)
print("Available Slots :", available)

# ------------------------------------------
# Find the first available slot

for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot Number :", i)
        break

# ------------------------------------------
# Display all available slot numbers

print("Available Slot Numbers:")

for i in range(len(slots)):
    if slots[i] == 0:
        print(i)

# ------------------------------------------
# Check whether parking occupancy exceeds 75%

occupancy_percentage = (occupied / len(slots)) * 100

print("Occupancy Percentage :", occupancy_percentage)

if occupancy_percentage > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")
