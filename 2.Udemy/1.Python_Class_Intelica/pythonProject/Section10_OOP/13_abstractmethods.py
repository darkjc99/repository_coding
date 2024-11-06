from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self): ...

    @abstractmethod
    def call_target(self, person: str): ...


class iBanana(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        raise NotImplementedError("Code missing...")

    def call_target(self, person: str):
        pass


phone = iBanana("iBanana")
print(phone.power)
