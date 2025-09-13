fruits = {
    "apple": 120,
    "banana": 40,
    "mango": 150,
    "grapes": 80,
    "orange": 60
}
min_cost = 200
sasta = ""

for fruit,price in fruits.items():
    if price < min_cost:
        min_cost = price
        sasta = fruit

print("sabse sasta",sasta,"price",min_cost)