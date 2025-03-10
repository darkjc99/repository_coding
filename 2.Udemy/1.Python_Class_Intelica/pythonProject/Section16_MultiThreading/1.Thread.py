import threading
import time


def process_data(name: str, count: int):
    print(f"Starting {name}")

    for i in range(count):
        print(name, i + 1, sep=":")
        time.sleep(1)


if __name__ == "__main__":
    thread_one = threading.Thread(target=process_data, args=("Thread-1", 10))
    thread_two = threading.Thread(target=process_data, args=("Thread-2", 5))

    thread_one.start()  # Inicia la ejecución de thread_one
    time.sleep(3)  # Espera 3 segundos antes de iniciar thread_two
    thread_two.start()  # Inicia la ejecución de thread_two

    thread_one.join()  # Espera a que thread_one termine
    thread_two.join()  # Espera a que thread_two termine
    
    
