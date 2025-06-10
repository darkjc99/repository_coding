def isValid(s: str) -> bool:
    mapping: dict = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False

    return not stack


print(isValid("([])"))
