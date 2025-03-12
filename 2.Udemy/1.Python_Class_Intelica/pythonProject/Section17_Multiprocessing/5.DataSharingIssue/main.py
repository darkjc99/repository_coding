from multiprocessing import Process

numbers: list[int] = [0]


def func():
    global numbers

    numbers.extend([1, 2, 3])
    print(f"Process data: {numbers}")


def main():
    process = Process(target=func)
    process.start()
    process.join()

    print("Main data:", numbers)


if __name__ == "__main__":
    main()
