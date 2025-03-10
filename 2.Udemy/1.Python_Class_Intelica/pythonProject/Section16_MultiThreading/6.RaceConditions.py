import threading
import time

lock = threading.Lock()


def edit(operation: str, amount: int, repeat: int):
    global value

    lock.acquire()
    for _ in range(repeat):
        temp: int = value
        time.sleep(0)
        if operation == "add":
            temp += amount
        elif operation == "subtract":
            temp -= amount
        time.sleep(0)
        value = temp

    lock.release()


if __name__ == "__main__":
    value: int = 0
    adder = threading.Thread(target=edit, args=("add", 100, 1_000_000))
    subtractor = threading.Thread(target=edit, args=("subtract", 100, 1_000_000))

    adder.start()
    subtractor.start()

    print("Waiting for threads to finish...")
    adder.join()
    subtractor.join()

    print(f"{value = }")
