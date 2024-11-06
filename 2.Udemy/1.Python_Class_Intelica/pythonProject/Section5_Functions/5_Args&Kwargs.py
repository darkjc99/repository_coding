def greet_people(age, *people: str): #Tuple
    print(people)
    for name in people:
        print(f"Hello {name}!")


#greet_people(10, "Luigi", "Toad")

def do_something(*args,**kwargs): # Dictionary
    print(args)
    print(kwargs)

    print(kwargs['name'])

do_something('Hello',name='Mario',age=10)