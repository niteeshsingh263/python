units = float(input("enter a  consumed unit here :"))

if units <=100:
  bill = units*5
  

elif units < 200:
  bill = units*7

else:
  bill = 100*5 + 100*7 + (units-200)*10
  print("total bill : ",bill)

