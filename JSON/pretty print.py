# Pretty Print following JSON data
import json

student_data = {"name":"david","age" :13,"marks":87}
data = json.dumps(student_data, indent=4,separators=(",","="))
print(data)
print(type(data))