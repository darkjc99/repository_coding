names: list[str] = ["Robert", "Mario", "Sofia", "James"]

for i, name in enumerate(names):
    print(i, ":", name)


for i in enumerate(names, start=1):
    print(i)
