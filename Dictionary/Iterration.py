student = {"name":"John","class":"8th","roll no":23}

# printing all the key names one by one
for i  in student:
    print(i)

# printing all the values name one by one

for i in student:
    print(student[i])

# using function

for i in student.values():
    print(i)

# using item function
for i,j in student.items():
    print(i ,"-" ,j )# jabb keys and value dono ek sath print karani ho tabb ye use krte hai