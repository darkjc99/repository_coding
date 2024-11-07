import math

var: str = "text"


def hello():
    hello_str: str = "str"
    hello_int: str = "str"

    def inner():
        pass

    print(locals())


if __name__ == "__main__":
    hello()
    print(locals())
