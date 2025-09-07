print("*******AREA CALCULATOR********")

while True:
   print("""Press 1 to get the area of square
   press 2 to get the area of rectangle
   press 3 to get the area of circle
   prees 4 to get the area of triangle""")


choice = int(input("enter a numer 1 -4 :"))

if choice == 1:
   while True:

       side = float(input("enter the legnth of one side"))
       area = side * side
       print("the area of square",area)
       repeat = input("do you want to try again square?")
       if repeat == "no":
          break

elif choice == 2:
  while True:
      length = float(input("enter the lenght  of rectangular"))
      width = float(input("enter the width of rectangle"))
      area = length* width
      print("the area of rectangle",area)
      repeat = input("do you want to try again rectangle? ")
      if repeat == "no":
          break

elif choice == 3:
   while True:
       radius= float(input("enter the radius of the circle"))
       area = 3.1416*radius**2
       print("the area of circle",area)
       repeat = input("do you want to try again circle? ")
       if repeat == "no":
          break
    

elif choice ==4:
    while True:
   
       base = float(input ("enter the base of Triangle"))
       height= float(input("enter the height of Triangle"))
       area= (1/2)*base*height
       print("the area of tringle",area)
       repeat = input("do you want to try again triangle?")
       if repeat == "no":
        break
        
else:
   print("invalid input")
       
repeat1 = input("do you want to again the  menu?(yes/no)")
if repeat1 == "no":
   print("exiting ........thank you")
   break