num = int(input("enetr a number here :"))
temp = num
rev = 0 

while num>0:
    digit = num %10
    rev = rev*10+digit
    num = num//10

if rev == temp:
    print("it  is pallendrome")
    

else:
    print("it is not pallendrome")
    