"""for i in range(1,6):
    for j in range(i,0,-1):
       print(j ,end ="  ")

    print()"""

    # reverse number

n=46123

rev = 0
while n > 0:
    digit = n%10
    rev = rev*10+ digit
    n = n//10

print("reverse",rev)

for i in range(1,101):
   if i % 7==0:
       print(i,end=",")
    