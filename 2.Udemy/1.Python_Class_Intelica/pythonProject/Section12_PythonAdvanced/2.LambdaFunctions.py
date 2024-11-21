def square(a: float) -> float:
    return a**2


sq = lambda a: a**2

print(square(4))
print(sq(4))


numbers: list[str] = [1, 2, 3, 4, 5, 6, 7]
even: list[int] = list(filter(lambda a: a % 2 == 0, numbers))

print(even)
