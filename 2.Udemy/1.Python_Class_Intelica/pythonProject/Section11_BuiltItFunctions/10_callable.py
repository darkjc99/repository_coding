a: str = "a"


def do_something():
    pass


def b():
    pass


if __name__ == "__main__":
    print(callable(a))
    print(callable(do_something))
    print(callable(b))
