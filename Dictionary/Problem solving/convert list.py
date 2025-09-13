fruits = {
    "apple": 120,
    "banana": 40,
    "mango": 150,
    "grapes": 80,
    "orange": 60
}

# dictionary ko list me convert kro

d = list(fruits.keys())
print(d)

# sum nikalna hai sabka
sum = 0
for i in fruits:
    sum += fruits[i]
    
print(sum)

# sabse mahenga fruits nikalao

max_cost = 0
mahega = ""

for fruit, price in fruits.items():
    if price > max_cost:
        max_cost = price
        mahega = fruit

print("sabse mahega fruit",mahega,"price",max_cost)
    