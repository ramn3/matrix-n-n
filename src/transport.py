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
    def __init__(self, name, x1):
        super().__init__(name, x1)

    def exat(self):
        print("машина")
        print("еду по дороге")


class airplane(transport):
    def __init__(self, name, x2):
        super().__init__(name, x2)

    def exat(self):
        print("самолет")
        print("лечу по воздуху")


class ship(transport):
    def __init__(self, name, x3):
        super().__init__(name, x3)

    def exat(self):
        print('корабль')
        print("плыву по воде")


mashina = car('бэха', 'крутая')
mashina.exat()
print(mashina)

print()

samolet = airplane('бизнесджет', 'ваще крутой')
samolet.exat()
print(samolet)

print()

korabl = ship('катамаран', 'слишком крутой')
korabl.exat()
print(korabl)
