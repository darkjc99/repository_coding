class Fruit:
    def __init__(self, name:str, calories:str):
        self.name = name
        self.calories = calories


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    

if __name__=='__main__':
    fruit_a: Fruit = Fruit('Banana',10)
    fruit_b: Fruit = Fruit('Banana',10)

    print(f'a:{id(fruit_a)}, b: {id(fruit_b)}')

    print(f'fruits_a is fruit_b = {fruit_a is fruit_b}')
    print(f'fruits_a == fruit_b = {fruit_a == fruit_b}')