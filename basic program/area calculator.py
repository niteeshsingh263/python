print("*******AREA CALCULATOR********")

print("""Press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
prees 4 to get the area of triangle""")

choise = int(input("enter a numer 1 -4 :"))

if choise == 1:

   side = float(input("enter the legnth of one side"))
   area = side * side
   print("the area of square",area)

elif choise == 2:

   length = float(input("enter the lenght  of rectangular"))
   width = float(input("enter the width of rectangle"))
   area = length * width
   print("the area of rectangle",area)

elif choise == 3:
   radius= float(input("enter the radius of the circle"))
   area = 3.1416*radius**2
   print("the area of circle",area)

elif choise ==4:
   
    base = float(input ("enter the base of Triangle"))
    hight= float(input("enter the hight of Triangle"))
    area= (1/2)*base*hight
    print("the area of tringle",area)

else:
   print("invalid input")
    







