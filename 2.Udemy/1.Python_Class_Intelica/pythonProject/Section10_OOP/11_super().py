class Lamp:
    def __init__(self, name: str):
        self.name = name

    def turn_on(self):
        print(f"Turning on: {self.name}")

    def turn_off(self):
        print(f"Turning off: {self.name}")


class ElectricLamp(Lamp):
    def __init__(self, name: str):
        super().__init__(name)

    def turn_on(self):
        print("Using electricity...")
        super().turn_on()


el_lamp: ElectricLamp = ElectricLamp("Bob")
el_lamp.turn_on()
