# Soet the following JSon keys and write them into aa file

import json

student_data = {"name":"david","age" :13,"marks":87}
f = open("data.json","w")
data = json.dumps(student_data , indent=4,sort_keys=True)
f.write(data)
print("the data has been adddd to the file")
