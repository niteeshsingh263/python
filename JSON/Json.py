# Convert the following DIctionary into JSON Formate
import json

student_data = {"name":"david","age" :13,"marks":87}
print(type(student_data))
data = json.dumps(student_data)
print(data)
print(type(data))