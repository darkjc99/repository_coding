class Fruit:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        print(f"{self._name} is being accessed!")
        return self._name

    @name.setter
    def name(self, value: str):
        print(f"{self._name} is now: {value}!")
        self._name = value


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple")
    apple.name = "Banana"
    print(apple.name)
