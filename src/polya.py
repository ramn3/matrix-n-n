class Class11A:
    def __init__(self):
        self.__name = None
        self.__old = None
        self.__character = None

    def get_name(self):
        return self.__name

    def get_old(self):
        return self.__old

    def get_character(self):
        return self.__character

    def set_name(self, value):
        self.__name = value

    def set_old(self, value):
        self.__old = value

    def set_character(self, value):
        self.__character = value


obj = Class11A()
obj.set_name('Славуся')
obj.set_old(12)
obj.set_character('скверный')
print(obj.get_name())
print(obj.get_old())
print(obj.get_character())