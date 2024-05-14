class Toy:
    def __init__(self, name):
        self.name = name


class Transport(Toy):
    def __init__(self, name, surname):
        super().__init__(name)
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"транспорт - {self.name}, свойство - {self.surname}"


class Car(Transport):
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)

    def exat(self):
        return "еду по дороге"


class Airplane(Transport):
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)

    def exat(self):
        return "лечу по воздуху"


class Ship(Transport):
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)

    def exat(self):
        return "плыву по воде"


transport = [
    Car('бэха', 'крутая'),
    Airplane('бизнесджет', 'ваще крутой'),
    Ship('катамаран', 'слишком крутой')
]

for transport in transport:
    print(f"{transport}")
    print(f"{transport.exat()}")
    print()
