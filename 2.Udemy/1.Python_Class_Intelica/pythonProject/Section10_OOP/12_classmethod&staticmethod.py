class Calculator:
    def __init__(self, name: str):
        self.name = name

    def description(self):
        print(f"{self.name} is a calculator!")

    @staticmethod
    def add_number(a: float, b: float):
        print(a + b)

    @classmethod
    def create_with_version(cls, name: str, version: int):
        return cls(f"{name}:({version})")


calc: Calculator = Calculator.create_with_version("Bob", 100)
calc.description()
