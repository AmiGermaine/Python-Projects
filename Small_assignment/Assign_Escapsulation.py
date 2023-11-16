
class Car:
    def __init__(self):
        self.__Name="2023"

    def getName(self):
        print(self.__Name)

    def setName(self, Kia):
        self.__Name = Kia


whitecar = Car()
whitecar.setName('EV6')
kia=whitecar.getName()
print('2023')
