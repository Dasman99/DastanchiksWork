# Реализовать концепцию **гибридного наследования** на основе организации IT-RUN,
# с элементами концепций *инкапсуляции*, *полиморфизма* и *абстракции*.

class Meta:
    def __init__(self, ceo, industry):
        self.ceo = ceo
        self.__industry = industry

    def info(self):
        return f'{self.ceo}, {self.__industry}'

class Managment(Meta):
    def __init__(self, coo):
        super().__init__()
        self.name = coo
        # self.__chief_oo = chief_operating_officer

    def info(self):
        return f'{self.name}'

class Board_of_directors(Meta):
    def __init__(self, director):
        super().__init__()
        self.direct = director
        # self._coo = coo

    def info(self):
        return f'{self.ceo}'

class MarkZuckerberg():
    def __init__(self, ceo, age):
        # super().__init__(self, ceo)
        self.name = ceo
        self.age = age


    def info(self):
        return f'A {self.name} is {self.age}'


# obj = Meta('Meta', 'Social Media')
# obj1 = Managment('Mark Zuckerberg')
# obj2 = Board_of_directors('Mark Zuckerberg')
obj3 = MarkZuckerberg('Mark', 38)
# print(obj.info())
# print(obj1.info())
# print(obj2.info())
print(obj3.info())

