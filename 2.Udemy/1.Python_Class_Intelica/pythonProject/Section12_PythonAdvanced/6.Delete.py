from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    calories: float


apple: Fruit = Fruit("Apple", 30)

print(apple)

del apple

print(apple)


"""people: list[str] = ["Mario", "Toad"]

del people[1]

print(people)

data: dict = {"field1": 100, "field2": 200}

del data["field2"]

print(data)

name: str = "Mario"

del name

print(name)"""
