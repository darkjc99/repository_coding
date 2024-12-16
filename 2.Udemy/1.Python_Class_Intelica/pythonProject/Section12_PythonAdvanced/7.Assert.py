import random


def start_program(data: dict):
    """This starts the program"""
    assert isinstance(data, dict), "Invalid JSON"
    assert data, "No data found..."

    print("Program loaded succesfully!")


if __name__ == "__main__":
    json: dict = {"name": "mario"}
    # json: dict = {}
    # json: str = "asdasda"
    start_program(data=json)

    print(__debug__)
