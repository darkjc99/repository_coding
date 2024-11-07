#user_input: str = input("Your code: ")
user_defined_code = """
x = 10
print(x)

for i in range(10):
    print(i,end=' ')
"""
exec(user_defined_code)
