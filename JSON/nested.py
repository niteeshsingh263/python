# Acces the nested key "marks" fromn the following nasted data

import json
student_data = """{ "student" :
                    { "grade":
                        {"name" : "david","marks" :87}
   
                      }
                  }"""
data = json.loads(student_data)
print (data["student"]["grade"] ["marks"])