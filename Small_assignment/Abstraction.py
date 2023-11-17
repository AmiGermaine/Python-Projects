
from abc import ABC,abstractclassmethod

class Animal(ABC):
    def favoriteSnack(self):
        pass

class Dog(Animal):
    def favoriteSnack(self):
        print('Love pup-peroni')

class Rabbit(Animal):
    def favoriteSnack(self):
        print('carrots')  

class Turkey(Animal):
    def favoriteSnack(self):
        print('kale') 

pet = Dog()
pet.favoriteSnack()

food = Turkey()
food.favoriteSnack()

cute = Rabbit()
cute.favoriteSnack()

