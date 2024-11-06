from enum import Enum


class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


c = Color.RED


def check_color(color: Color):
    if color == Color.RED:
        print(color)
    elif color == Color.BLUE:
        print(color)
    elif color == Color.GREEN:
        print(color)


check_color(Color.BLUE)
