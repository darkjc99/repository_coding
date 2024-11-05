class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.model} ({self.color})'

    def __repr__(self):
        return f'Car(model={self.model}, color={self.color})'

if __name__ == '__main__':
    car = Car = Car('BWM','Blue')
    print(car)
    print(car.__repr__())
