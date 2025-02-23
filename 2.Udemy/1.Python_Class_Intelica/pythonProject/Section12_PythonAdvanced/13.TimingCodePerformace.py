import time
import timeit

# def time_func(func):
#     start_time: float = time.perf_counter()

#     for i in range(10**5):
#         pass

#     print("Hello")
#     time.sleep(1)

#     end_time: float = time.perf_counter()

#     print(f"Total time: {end_time - start_time} seconds")


def make_calculation(first: int, second: int) -> int:
    for i in range(10**3):
        pass

    return first + second


def do_something():
    for i in range(10):
        x: int = i**i


def get_time(func: str, repeat: int, number: int) -> float:
    speed: float = min(
        timeit.repeat(func, repeat=repeat, number=number, globals=globals())
    )
    print(f"{func} -> {round(speed, 4)} sec (ran {repeat * number:,}) times")
    return speed


if __name__ == "__main__":
    a, b = 1, 2
    get_time("do_something()", repeat=10, number=10**5)
    get_time("make_calculation(a,b)", repeat=10, number=10**5)
