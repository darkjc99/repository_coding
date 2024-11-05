class Lamp:
    def __init__(self, name: str, model: int, version: int):
        self.name = name
        self.__model = model #private attribute
        self._version= version #protected attribute

    def description(self):
        self.__self_mainteance()
        print(self.name, self.__model)

    def __self_mainteance(self):
        print(self.name, 'is fixing itself.')

class ElectricLamp(Lamp):
    def __init__(self, name: str, model: int, version: int):
        super().__init__(name, model, version)

    def do_something(self):
        print(self._version)

lamp : Lamp = Lamp('Lamp',1010,123456)
lamp.description()

el_lamp: ElectricLamp = ElectricLamp('ElLamp',1010,123456)
el_lamp.do_something()
print(el_lamp._version)


