
class Car:
    def __init__(self):
        self.__Name="2023" # Private attribute
        self._origin = "" # Protectecd attribute

    def getName(self):
        print(self.__Name)

    def setName(self, Kia):
        self.__Name = Kia


whitecar = Car()
whitecar.getName() # Original name before change.
whitecar.setName('EV6')
whitecar.getName() # New Name

whitecar._origin = "Japan"
print(whitecar._origin) # print protected attribute.