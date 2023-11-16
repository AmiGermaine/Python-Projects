# Private attribute
class Car:
    def __init__(self):
        self.__lName="2023"

    def getName(self):
        print(self.__Name)

    def setName(self, Kia):
        self.__Name = Kia


whitecar = Car()
whitecar.setName('EV6')
kia=whitecar.getName()
print('kia')
print('2023')

# Protectecd attribute
def Country(self):
    self._origin = ""

whitecar._origin = "Japan"
print(whitecar._origin)