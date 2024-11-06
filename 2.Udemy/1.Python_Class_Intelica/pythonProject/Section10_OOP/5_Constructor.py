class Fruit:
    def __init__(self, name: str):
        self.name = name
        self.letter_count = len(name)
        print("Constructor called")


fruit: Fruit = Fruit("Banana")
fruit.name = "Banana"
print(fruit.name)
print(fruit.letter_count)
