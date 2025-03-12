from time import sleep
from multiprocessing import Process, Lock, Semaphore


def func(p_lock, identifier):
    with p_lock:
        sleep(1)
        print(f">>Process {identifier} is running...")


def main():
    lock = Lock()
    sem = Semaphore(3)

    processes = [Process(target=func, args=(sem, i)) for i in range(5)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
