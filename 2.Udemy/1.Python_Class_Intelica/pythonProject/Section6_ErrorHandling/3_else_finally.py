user_input: str = input("You: ")

try:
    number = float(user_input)
    print(number)
except Exception as e:
    print("Exception:", e)
else:
    print("Successfully executed code!")
finally:
    print("This will always run!")