status: int = 405

match status:
    case 400:
        print("Bad request...")
    case 403:
        print("Forbidden...")
    case 404:
        print("Not found...")
    case _:
        print("Something went wrong...")


user_input: str = input("Command: ")
p_command: list[str] = user_input.split()
print(p_command)

match p_command:
    case ["find", *images]:
        print(f"Finding: {images}")
    case ["download", *images]:
        print(f"Downloading: {images}")
    case ["cancel" | "delete", *images] if len(images) > 1:
        print(f"Deletting: {images}")
    case _:
        print("Command not recognised...")
