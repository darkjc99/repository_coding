# from functools import wraps
# from time import perf_counter
# import sys

# def memoization(func):
#     cache: dict = {}

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key: str = str(args) + str(kwargs)

#         if key not in cache:
#             cache[key] = func(*args, **kwargs)
#         return cache[key]

#     return wrapper


# @memoization
# def fibonacci(n) -> int:
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


# if __name__ == "__main__":
#     start: float = perf_counter()
#     f: int = fibonacci(100)
#     end: float = perf_counter()

#     print(f)
#     print(f"Time: {end - start} seconds!")

import functools
from time import perf_counter
import sys

@functools.cache
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    start: float = perf_counter()
    f: int = fibonacci(100)
    end: float = perf_counter()

    print(f)
    print(f"Time: {end - start} seconds!")
