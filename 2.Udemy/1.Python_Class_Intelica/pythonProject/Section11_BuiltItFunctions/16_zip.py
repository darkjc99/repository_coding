people = ("Mario", "Luigi", "Toad", "Bowser")
numbers = (10, 20, 30)
letters = ("a", "b", "c")

zipped = zip(people, numbers, letters)

for item in zipped:
    print(item)
