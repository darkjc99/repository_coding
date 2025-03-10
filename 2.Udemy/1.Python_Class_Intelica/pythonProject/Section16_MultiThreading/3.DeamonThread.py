import threading
import time


def infinite_loop():
    while True:
        print(time.time())
        time.sleep(1)


if __name__ == "__main__":
    thread = threading.Thread(target=infinite_loop, daemon=True)
    thread.start()
    
    
    