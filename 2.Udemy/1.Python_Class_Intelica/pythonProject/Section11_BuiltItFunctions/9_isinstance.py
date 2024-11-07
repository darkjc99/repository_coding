class Fruit:
    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple")
    banana: Fruit = Fruit("Banana")

    # print(isinstance(apple, Fruit))
    # print(isinstance(banana, Fruit))
    # print(isinstance("string", str))
    # print(isinstance(10, str))

    if isinstance(apple, Fruit):
        print("Apple is a fruit")
    elif isinstance(apple, str):
        print("This string is crazy!")
