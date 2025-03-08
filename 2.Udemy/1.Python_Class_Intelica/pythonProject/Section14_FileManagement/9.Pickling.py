import pickle

# text: str = "text"
# number: int = 10

# with open("save.txt", "w") as file:
#     file.write(text + "\n")
#     file.write(str(number) + "\n")

# with open("save.txt", "r") as file:
#     'Fruit('Banana')'
#     print(file.read())


class Fruit:
    def __init__(self, name, calories: float):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print({self.name, ":", self.calories})


if __name__ == "__main__":
    # fruit: Fruit = Fruit("Banana", 100)

    # fruit.calories = 150

    # with open('save.pickle', 'wb') as file:
    #     pickle.dump(fruit, file)

    with open("save.pickle", "rb") as file:
        fruit: Fruit = pickle.load(file)

    print(fruit.describe_fruit())
