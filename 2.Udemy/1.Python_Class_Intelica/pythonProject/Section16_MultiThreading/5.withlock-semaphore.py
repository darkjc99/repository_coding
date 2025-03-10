import threading
import time

# sem = threading.Semaphore(5)
lock = threading.Lock()

def process_something(id: int):
    with lock:
        print(f"{id} -> Running!")
        time.sleep(1)
        print(f"{id} -> Finished!")


if __name__ == "__main__":
    for i in range(10):
        time.sleep(0.5)
        thread = threading.Thread(target=process_something, kwargs={"id": i + 1})
        thread.start()
