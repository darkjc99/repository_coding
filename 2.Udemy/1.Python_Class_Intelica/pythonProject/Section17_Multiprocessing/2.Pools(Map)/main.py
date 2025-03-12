import multiprocessing as mp
from time_stuff import get_time, kill_time
import time


def convert_to_x(number: int) -> str:
    time.sleep(2)
    # kill_time()
    return number * "x"


@get_time
def main():
    print(f"Cores available: {mp.cpu_count()}")

    values: tuple[int, ...] = tuple(range(1, 9))

    with mp.Pool(processes=4) as pool:
        results: list[str] = pool.map(convert_to_x, values)
        print("Results:", results)


if __name__ == "__main__":
    main()
