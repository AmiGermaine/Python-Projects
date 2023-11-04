#parent class
class Pets:
    name = "No Name Provided"
    Weight = 0
            
# Dog and Cat are child class, that will inherit name and weight attributes from Pets class
class Dog(Pets):
    def __init__(self,name):
        self.name = name
    fur_color = "Brown"
    breed = "bulldog"

class Cat(Pets):
   eye_color = "gray"
   personality = "angry"


cat1 = Cat()
cat1.name = "rose"
print(cat1.eye_color)
cat1.eye_color = 'green'
print(cat1.personality)
print(cat1.eye_color)
print(cat1.name)
dog2 = Dog('dill')
print(dog2.name)
dog3 = Dog('Sandy')
print(dog3.name)
dog4 = Pets()
print(dog4.name)
dog4.name = "jr"
print(dog4.name)