from dataclasses import dataclass


@dataclass
class Fruit2:
    name:str,
    calories : float


class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple", 10)
    apple2: Fruit = Fruit("Apple", 10)

    print(apple == apple2)
