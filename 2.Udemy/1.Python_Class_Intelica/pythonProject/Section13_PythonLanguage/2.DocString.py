import math
import random

def get_length(item: str) -> int:
    """Returns the total lenght of a string(excl. spaces)

    :param str item: The item that you want to get the length of
    :return: The length of the item as an int.
    :raises TypeError: If item is not a str
    """

    if isinstance(item, str):
        processed: str = "".join(item.split())
        return len(processed)
    else:
        raise TypeError(f"item is not a str")


length: int = get_length("Hello, World")
print(length) 