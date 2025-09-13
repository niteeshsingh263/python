student = {'Amit': 89, 'Ravi': 90, 'Abhay': 92, 'Sohan': 88}

topper = max(student, key = student.get)
print("topper",topper,"marks",student[topper])

max_marks = 0
topper = ""

for name , marks in student.items():

    if marks> max_marks:
      max_marks = marks
      topper = name

print("topper",topper,"marks",max_marks)