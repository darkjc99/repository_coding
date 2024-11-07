numbers: list[int] = [1, 2, 3, 4, 5, 6]


def convert_to_string(element):
    element *= element
    return str(element)


converted_list: list[str] = list(map(convert_to_string, numbers))

print(converted_list)
