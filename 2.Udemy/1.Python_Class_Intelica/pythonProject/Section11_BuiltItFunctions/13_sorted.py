from unittest import removeResult


nums: list[int] = [1, 6, 2, 3, 4, 7, 5]
strings: list[str] = ["A", "b", "C", "d", "e", "F"]

nums.sort()
print(nums)

sorted_numbers: list[int] = sorted(nums, reverse=True)
print(sorted_numbers)

sorted_string: list[str] = sorted(strings, key=str.lower)
print(sorted_string)


class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"


fruits: list[Fruit] = [
    Fruit("Apple", 50),
    Fruit("Banana", 150),
    Fruit("Anana", 100),
]


def sort_by_calories(fruit: Fruit):
    return fruit.calories


def sort_by_name(fruit: Fruit):
    return fruit.name


sorted_fruits: list[Fruit] = sorted(fruits, key=str, reverse=True)
print(sorted_fruits)
