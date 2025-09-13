
student = {}

while True: 

    name= input("enter student name here(or type stop then finis):")
    if name.lower() == "stop":
      break

    marks = int(input(f"enter marks of {name}: "))
    student[name] = marks

print("\n ---- student records-----")
for name , marks in student.items():
   print(name,"->",marks)

