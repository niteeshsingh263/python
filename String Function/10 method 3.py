#endswith
a = "harry potter"

print(a.endswith("r"))

#startswith

a= "hrry potter"

print(a.startswith("h"))# range bhi de sakte

#swapcase()

a = "harry potter"
b = "HARRY POTTER"
print(a.swapcase())
print(b.swapcase())

#strip()

a= "********harry potter*******"
print(a.strip("*, "))

#split()

a = "hello . my name is niteesh.and iam 23"
print(a.split("."))

#ljust()

a = "harry potter"
x = a.ljust(30,"-")
print(x,"is a my fav movie")

#rjust()

a = "hary potter"
x = a.rjust(20,"-")
print(x,"is a my fav movie")

#replce()

a = "My Name Is Abhay"
print(a.replace("Abhay","Niteesh"))

#rindex

a = "My Name Is a Niteesh Singh"
print(a.rindex("Niteesh"))

#rfind()

a = "bibidy bibidy boo"
print(a.rfind("dy",0,9))