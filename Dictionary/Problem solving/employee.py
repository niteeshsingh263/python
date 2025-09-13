employees = {
    "emp1": {
        "name": "Rahul",
        "salary": 50000,
        "department": "IT"
    },
    "emp2": {
        "name": "Sneha",
        "salary": 60000,
        "department": "HR"
    },
    "emp3": {
        "name": "Amit",
        "salary": 55000,
        "department": "Finance"
    },
    "emp4": {
        "name": "Priya",
        "salary": 70000,
        "department": "Marketing"
    }
}

# rint(employees)

max_sallery = 0
highsalery = ""

for emp_id,details in employees.items():
    if details["salary"] > max_sallery:
        max_sallery= details["salary"]
        highsalery = details["name"]

print("sabse jyda salery",highsalery,"salery",max_sallery)