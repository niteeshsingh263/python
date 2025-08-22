amount = int(input("enter your shoping amount here:"))

if amount >=500:
    discount = (amount*20)/100
    print("discount",discount )
    print("final amount",amount - discount)

elif amount >=200 and amount<500:
    discount = (amount*10)/100
    print("apply discount",discount)
    print("final bill",amount-discount)

else:
    print("no discount")