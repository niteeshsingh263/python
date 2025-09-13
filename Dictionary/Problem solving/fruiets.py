fruits = {
    "apple": 120,
    "banana": 40,
    "mango": 150,
    "grapes": 80,
    "orange": 60
}

# 5 fruits print
print(fruits)

# Apple ki price print kro

print("apple",fruits["apple"])

# mango ki price ko update krke 120 kro

fruits.update({"mango":120})
print(fruits)

# banana ko delte kro

del fruits["banana"]
print(fruits)

# check kro orenge hai dictionary me ya nhi

if "orange" in fruits:
    print("orenge hai dictionary me")
    

else:
    print("orenge not in dictionary")
        