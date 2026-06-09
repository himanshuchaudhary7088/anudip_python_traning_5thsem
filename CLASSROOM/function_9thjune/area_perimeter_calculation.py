#create a program which provides the menu to the user to select the 2d figure(circle,rectangle,square) after selecting figure user is again asked them to provide the input of corresponding data for the figure .after input of corresponding data again provide a menu to select the operation(area/perimeter)and as per the data provided by user display the resultof operation this take will be repeated again and again until user select the operation toexit from the figure .

#to import a module
from geometry import*
#--- main program ---
print("Welcome to the Geometry Calculator!")
#provide menu to user to select the 2d figure
while True:

    print("\n===== FIGURE MENU =====")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Square")
    print("4. Exit")

    figure = int(input("Enter Figure Choice: "))

    # Exit
    if figure == 4:
        print("Program Terminated")
        break

    # Invalid Figure Choice
    if figure < 1 or figure > 4:
        print("Invalid Figure Choice")
        continue

    # ---------------- Rectangle ----------------

    if figure == 1:

        length = float(input("Enter Length: "))
        if length <= 0 :
            print("Length must be greater than 0")
            continue
        
        breadth = float(input("Enter Breadth: "))
        if breadth <= 0 :
            print("Breadth must be greater than 0")
            continue

        while True:

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                print("Area =", area_of_rectangle(length, breadth))

            elif choice == 2:
                print("Perimeter =", perimeter_of_rectangle(length, breadth))

            elif choice == 3:
                break

            else:
                print("Invalid Operation Choice")

    # ---------------- Circle ----------------

    elif figure == 2:

        radius = float(input("Enter Radius: "))

        if radius <= 0:
            print("Radius must be greater than 0")
            continue

        while True:

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                print("Area =", area_of_circle(radius))

            elif choice == 2:
                print("Perimeter =", perimeter_of_circle(radius))

            elif choice == 3:
                break

            else:
                print("Invalid Operation Choice")

    # ---------------- Square ----------------

    elif figure == 3:

        side = float(input("Enter Side: "))

        if side <= 0:
            print("Side must be greater than 0")
            continue

        while True:

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Change Figure")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                print("Area =", area_of_square(side))

            elif choice == 2:
                print("Perimeter =", perimeter_of_square(side))

            elif choice == 3:
                break

            else:
                print("Invalid Operation Choice")