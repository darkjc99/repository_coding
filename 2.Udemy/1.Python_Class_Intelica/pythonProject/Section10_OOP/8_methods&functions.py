class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def explode(self):
        print(self.name, 'exploded!')

    def eat(self):
        print(self.name, 'has been eaten!')
def hello():
    print('Hello')

Fruit('Banana',10).eat()
hello()