from multiprocessing import Pipe


def main():
    c1, c2 = Pipe(duplex=True)
    # c2.send("text")
    c1.send("Hello")
    print("Data to be received:", c2.poll())

    if c2.poll():
        obj = c2.recv()
        print(obj)
    print("Data to be received:", c2.poll())


if __name__ == "__main__":
    main()
