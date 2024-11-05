class Animal:
    tricks: list[str] = []

    def __init__(self, name: str):
        self.name = name

    def teach_trick(self, trick_name:str):
        self.tricks.append(trick_name)

if __name__ =='__main__':
    dog: Animal = Animal('Dog')
    cat: Animal = Animal('Cat')

    dog.teach_trick('Make dinner!')
    dog.teach_trick('Go work at a job!')
    cat.teach_trick('I am a cat')

    print('Dog tricks:', dog.tricks)
    print('Cat tricks:', cat.tricks)
