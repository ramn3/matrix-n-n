class toy:
    def __init__(self, name):
        self.name = name


class transport(toy):
    def __init__(self, name, surname):
        super().__init__(name)
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"транспорт - {self.name}, свойство - {self.surname}"


class car(transport):
    def __init__(self, name, characteristic):
        super().__init__(name, characteristic)

    def exat(self):
        print("машина")
        print("еду по дороге")


class airplane(transport):
    def __init__(self, name, characteristic):
        super().__init__(name,characteristic)

    def exat(self):
        print("самолет")
        print("лечу по воздуху")


class ship(transport):
    def __init__(self, name, characteristic):
        super().__init__(name,characteristic)

    def exat(self):
        print('корабль')
        print("плыву по воде")


car = car('бэха', 'крутая')
car.exat()
print(car)

print()

airplane = airplane('бизнесджет', 'ваще крутой')
airplane.exat()
print(airplane)

print()

ship = ship('катамаран', 'слишком крутой')
ship.exat()
print(ship)
