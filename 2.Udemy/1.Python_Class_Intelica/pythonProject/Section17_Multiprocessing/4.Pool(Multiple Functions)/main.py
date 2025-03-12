import multiprocessing as mp
from time_stuff import get_time
import functools
import time


def func_a(param):
    time.sleep(2)
    return param


def func_b(param):
    time.sleep(2)
    return param


def func_c(param, param2):
    time.sleep(2)
    return param, param2


def map_func(func):
    return func


@get_time
def main():
    print(f"Cores available: {mp.cpu_count()}")

    a = functools.partial(func_a, "A")
    b = functools.partial(func_b, "B")
    c = functools.partial(func_c, "C", "C2")

    with mp.Pool() as pool:
        results = pool.map(map_func, [a, b, c])
        print("Results:", results)


if __name__ == "__main__":
    main()
