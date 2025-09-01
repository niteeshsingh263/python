while True:
    name = input("enter customers name")
    total = 0

    while True:
        print("enter the amount and quantity")
        quantity =float(input("enter quantity"))
        amount =  float(input("enter amount"))
        total += amount * quantity
        repeat = input("do you want tp add more items ? (yes/no:)")
        if repeat == "no" or repeat == "No":
            break 
      
    print("-"*40)
    print("Name",name)
    print("Ampunt to be paid",total)
    print("-"*40)
    print("*************happy shoping*********")

    repeat1= input("do you want to go to next customer? (yes/no)")
    if repeat1 == "no" or repeat1 == "No":
      break  