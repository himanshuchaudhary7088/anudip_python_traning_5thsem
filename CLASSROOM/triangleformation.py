#program to check three angles form a triangle
angle1 = float(input("enter the first angle: "))
#validate angle 1
if(angle1<0):
    exit("angle cannot be negative")
#........................................................
angle2 = float(input("enter the second angle: "))
#validate angle 2
if(angle2<0):
    exit("angle cannot be negative")
#..............................................................    
angle3 = float(input("enter the third angle: "))
#validate angle 3
if(angle3<0):
    exit("angle cannot be negative")
#...........................................................
#veryfing triangle formation
if(angle1+angle2+angle3 == 180):
   print("triangle can form ")
else:
    print("triangle doesn't form")