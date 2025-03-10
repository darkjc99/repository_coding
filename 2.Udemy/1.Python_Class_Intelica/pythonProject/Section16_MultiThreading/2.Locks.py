import threading
import time

lock = threading.Lock()


def count(limit: int, name: str):
    for i in range(limit):
        time.sleep(0.5)
        print(name, i + 1, sep=":")


def task1():
    lock.acquire()
    t2 = threading.Thread(target=task2)
    t2.start()
    count(5, "T-1")
    lock.release()


def task2():
    lock.acquire()
    count(5, "T-2")
    lock.release()


def task3():
    count(5, "T-3")


def main():
    t1 = threading.Thread(target=task1)
    t1.start()


if __name__ == "__main__":
    main()
