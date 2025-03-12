from multiprocessing import Process, Queue
import time


def square_number(identifier: int, num: int, queue: Queue):
    time.sleep(2)
    queue.put((identifier, num**2))


def main():
    queue: Queue = Queue()

    data: list[int] = list(range(1, 9))

    processes = [
        Process(target=square_number, args=(identifier, num, queue))
        for identifier, num in enumerate(data)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    unsorted = [queue.get() for _ in processes]
    print(unsorted)

    result = [val[1] for val in sorted(unsorted)]
    print(result)


if __name__ == "__main__":
    main()
