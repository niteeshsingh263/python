n = int(input("enter a number here:"))

for i in range(1,n+1):
    if n % i==0:
       print(i,end = " ")
