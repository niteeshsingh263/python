
n= int(input("enter a number"))

if n< 1:
    print("it is a not prime")

if n > 1:
    for i in range(2,n):
        if n %i==0:
            print("it is a not prime number")
            break
        else:
            print("it is prime number")
            break