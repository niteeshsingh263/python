d = {1,4,6,32,45,67.56}
# clear
d.clear()
print(d)

# pop
a = {"a":9,"b":6}
print(a.pop("b"))
print(a)

#popitem
print(a.popitem())
print(a)

#setdefault
c = {"a":2}
print(c.setdefault("a",7))
print(c.setdefault("b",9))
print(c)

#fromkeys
keys = {"a","b","c"}
e = dict.fromkeys(keys,3)
print(e)

# update
f = {"a":2}
f.update({"b":4,"c":9})
print(f)