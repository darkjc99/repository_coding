import multiprocessing as mp
from time_stuff import get_time
import time


def add_numbers(*args) -> float:
    time.sleep(2)
    return sum(args)


@get_time
def main():
    print(f"Cores available: {mp.cpu_count()}")

    values = ((1, 2, 10), (3, 4), (5, 6), (7, 8, 111))
    with mp.Pool() as pool:
        results: list[float] = pool.starmap(add_numbers, values)
        print("Results:", results)


if __name__ == "__main__":
    main()
