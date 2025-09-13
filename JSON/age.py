# Acces the value of age from the given data.
import json
student_data = """{"name":"david","age" :13,"marks":87}"""  # agar hamm age ko acces krenge tho student data ko ham triple cotation me rakhnge

data = json.loads(student_data)
print(data["age"])