num = int(input("enter the number upto 5 digit"))

if num>=0 and num<=9:
    print("it is a single digit number")

elif num >=10 and num <=99:
    print("it is a doble digit number")   

elif num >= 100 and num <=999:
    print("number is triple digit")

elif num >= 1000 and num <=9999:
    print("number is fourth dight")

else:
    print("It is five digt number")