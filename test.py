d = {"token": 1234567890,
     "a": 4718923648912376,
     "b": 4710943190713794}
if set(d.keys()) == {"token", "a", "b"}:
    print("truuu")
else:
    print("nahh")

print(all(x >= 0 for x in list(d.values())))
print(all(isinstance(x, int) for x in list(d.values())))