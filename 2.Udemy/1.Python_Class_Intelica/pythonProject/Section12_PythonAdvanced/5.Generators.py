'''
    def generate_list(n: int):
    for i in range(n):
        yield i


if __name__ == "__main__":
    generator = generate_list(100)

    # print(next(generator))

    list_a: list[int] = []
    for number in generator:
        list_a.append(number)
        if number == 10:
            break

    print(list_a)

    list_b: list[int] = []
    for number in generator:
        list_b.append(number)
        if number == 20:
            break

    print(list_b)
'''

if __name__=='__main__':
    yield_comprehension = (i for i in range(100))

    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))
