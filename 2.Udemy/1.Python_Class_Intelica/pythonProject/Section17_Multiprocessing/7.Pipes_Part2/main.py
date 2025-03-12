from multiprocessing import Pipe, Process, current_process
from random import randint
import os
import time


def sender(connection):
    print(f"Sender:{current_process().name} ({os.getpid()})")

    for _ in range(5):
        rand: int = randint(1, 10)
        connection.send(rand)
        print(f"{rand} was sent ...")
        time.sleep(0.5)

    print("Sending: 'None'...")
    connection.send(None)
    print("Done with sending data!")


def receiver(connection):
    print(f"Receiver:{current_process().name} ({os.getpid()})")

    while True:
        data = connection.recv()
        print(f"{data} was received...")

        if data is None:
            break

    print("Done with receiving data!")


def main():
    c1, c2 = Pipe()
    s = Process(target=sender, args=(c2,))
    r = Process(target=receiver, args=(c1,))

    s.start()
    r.start()

    s.join()
    r.join()


if __name__ == "__main__":
    main()
