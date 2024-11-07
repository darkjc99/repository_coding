var: str = "GLOBAL"


def hello():
    return "GLOBAL"


class Fruit:
    def __init__(self):
        print("GLOBAL")

print(globals())
