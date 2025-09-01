n= int(input("enter number 1 to 50:"))

if n == 1:
    print("it is a not prime number")
if n >1: 
  for i in range(2,n):
      if n %i== 0:
           print(" not prime number")
           break
      else:
           print(" it is prime number")
           break
           
